# This code is inspired by the mcpt project by neurotrader888.
# Repository: https://github.com/neurotrader888/mcpt
# MIT License (c) 2025 neurotrader888

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def donchian_breakout(ohlc: pd.DataFrame, lookback: int) -> pd.Series:
    """
    Generates Donchian channel breakout signals.

    Parameters:
    ohlc (pd.DataFrame): DataFrame containing OHLC data with a 'Close' column.
    lookback (int): Lookback period for the Donchian channel.

    Returns:
    pd.Series: Trading signals (1 for buy, -1 for sell, 0 for hold).
    """
    if "Close" not in ohlc:
        raise ValueError("Input DataFrame must contain a 'Close' column.")

    upper = ohlc["Close"].rolling(lookback).max().shift(1)
    lower = ohlc["Close"].rolling(lookback).min().shift(1)

    signal = pd.Series(np.nan, index=ohlc.index)
    signal[ohlc["Close"] > upper] = 1
    signal[ohlc["Close"] < lower] = -1

    return signal.ffill().fillna(0)


def optimize_donchian(ohlc: pd.DataFrame, max_lookback: int = 168) -> tuple[int, float]:
    """
    Finds the optimal lookback period for the Donchian breakout strategy.

    Parameters:
    ohlc (pd.DataFrame): DataFrame containing OHLC data with a 'Close' column.
    max_lookback (int): Maximum lookback period to test.

    Returns:
    tuple: Best lookback period and corresponding profit factor.
    """
    if "Close" not in ohlc:
        raise ValueError("Input DataFrame must contain a 'Close' column.")

    best_profit_factor = 0.0
    best_lookback = -1
    log_returns = np.log(ohlc["Close"]).diff().shift(-1)

    for lookback in range(1, max_lookback + 1):
        signal = donchian_breakout(ohlc, lookback)
        strategy_returns = signal * log_returns

        total_positive = strategy_returns[strategy_returns > 0].sum()
        total_negative = strategy_returns[strategy_returns < 0].abs().sum()

        if total_negative > 0:
            profit_factor = total_positive / total_negative
            if profit_factor > best_profit_factor:
                best_profit_factor = profit_factor
                best_lookback = lookback

    return best_lookback, best_profit_factor


def plot_donchian(df: pd.DataFrame, signal: pd.Series, lookback: int) -> None:
    """Plots cumulative log returns for the Donchian breakout strategy."""
    if not {"Close", "Date"}.issubset(df.columns):
        raise ValueError("DataFrame must contain 'Close' and 'Date' columns.")

    df = df.copy()
    df["r"] = np.log(df["Close"]).diff().shift(-1)
    df["donch_r"] = df["r"] * signal

    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    plt.style.use("dark_background")
    df["donch_r"].cumsum().plot(color="green", figsize=(10, 5), label="Cumulative Log Return")

    plt.title(f"Donchian Breakout Strategy (Lookback = {lookback})")
    plt.ylabel("Cumulative Log Return")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        df = pd.read_csv("eth_clean.csv")
        df["Date"] = pd.to_datetime(df["Date"], format="mixed")

        best_lookback, best_profit_factor = optimize_donchian(df)
        print(f"Best Lookback: {best_lookback}, Best Profit Factor: {best_profit_factor:.2f}")

        signal = donchian_breakout(df, best_lookback)
        plot_donchian(df, signal, best_lookback)
    except Exception as error:
        print(f"Error: {error}")