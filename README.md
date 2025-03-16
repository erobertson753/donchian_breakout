# Donchian Channel Breakout Strategy

This project implements a **Donchian Channel Breakout Strategy** for analyzing and optimizing trading signals based on historical price data. The strategy generates buy/sell signals when the closing price breaks above or below the Donchian channel.

## Features
- **Donchian Breakout Signal Generation**: Identifies buy/sell signals based on price breakouts.
- **Lookback Period Optimization**: Finds the best lookback period by maximizing the **profit factor**.
- **Performance Visualization**: Plots the cumulative log returns of the strategy.

## Requirements
- Python 3.x
- Pandas
- NumPy
- Matplotlib

Install dependencies using:
```sh
pip install pandas numpy matplotlib
```

## Usage
### 1. Prepare Your Data
Ensure your dataset (`eth_clean.csv`) contains:
- `Date` column (datetime format)
- `Close` column (closing prices)

### 2. Run the Script
```sh
python donchian.py
```
The script:
1. Loads historical price data.
2. Finds the optimal lookback period.
3. Generates trading signals.
4. Plots the cumulative log returns.

### 3. Expected Output
- Optimal lookback period and corresponding profit factor.
- A plotted graph showing cumulative log returns over time.

## Example Output
```
Optimal Lookback: 24, Profit Factor: 1.75
```
(A figure displaying cumulative returns will also be generated.)

## License
This project is licensed under the MIT License. See the original **mcpt** project by **neurotrader888** for reference: [GitHub Repository](https://github.com/neurotrader888/mcpt).

