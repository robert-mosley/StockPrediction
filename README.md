# Stock Prediction
A python-based program that allows users to visualize historical stock data and predict future stock prices.

## Features

- **Show Stock Data**: You can plot historical data for a stock (e.g., High, Low, Open, Close).
- **Predict Stock Price**: Given a stock, the script will predict the stock price for a specified number of days based on previous data using a Linear Regression model.

## Requirements

- Python 3.x
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`
- `yfinance`
- `pandas_datareader`

## Usage

- Clone the repository or download the script to your local machine.
- Run the script from the command line: python stock_prediction.py <STOCK_SYMBOL>

You can install the necessary libraries by running:

```bash
pip install pandas numpy matplotlib scikit-learn yfinance pandas_datareader
