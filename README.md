# Donchian Channel Breakout Strategy

This project implements a **Donchian Channel Breakout Strategy** for analyzing and optimizing trading signals based on historical price data. The strategy generates buy/sell signals when the closing price breaks above or below the Donchian channel.

## Features
- **Donchian Breakout Signal Generation**: Identifies buy/sell signals based on price breakouts.
- **Lookback Period Optimization**: Finds the best lookback period by maximizing the **profit factor**.
- **Performance Visualization**: Plots the cumulative log returns of the strategy.

## Requirements
- **Python 3.x**
- **R** with `tidyverse`, `dplyr`, and `lubridate` packages
- `pandas`
- `numpy`
- `matplotlib`

Install dependencies using:
```sh
pip install pandas numpy matplotlib
```
and 
```sh
install.packages(c("lubridate", "dplyr", "tidyverse"))
```

## Usage
### 1. Prepare Your Data
The dataset is preprocessed using an R script before running the Python strategy. Ensure you have the original **`eth.csv`** file.

Run the cleaning script in R:
```sh
Rscript clean_eth_data.R
```

This script:
- Loads `eth.csv`, selecting the Unix timestamp and Close price.
- Converts timestamps to datetime format.
- Filters out invalid data and ensures the dataset is within the correct timeframe.
- Reverses the dataset to chronological order.
- Saves the cleaned dataset as **`eth_clean.csv`**.

### 2. Run the Strategy Script
```sh
python donchian.py
```

The script:
1. Loads **`eth_clean.csv`**.
2. Finds the optimal lookback period.
3. Generates trading signals.
4. Plots the cumulative log returns.

### 3. Expected Output
- **Optimal lookback period**, corresponding **profit factor**, and **total number of trades** executed by the strategy.
- A plotted graph showing the **cumulative log returns** of the **trading strategy** over time.
- A plotted graph showing the **cumulative log returns** of an **unmanaged long position** over time.

#### Example Output
```
Best Lookback: 43 hours, Best Profit Factor: 1.04, over 65,810 total trades
```
(Figures displaying cumulative returns of the trading strategy and unmanaged long position will also be generated.)

## License
This project is licensed under the **MIT License**. See the original **mcpt** project by **neurotrader888** for reference: [GitHub Repository](https://github.com/neurotrader888/mcpt).

