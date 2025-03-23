from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
from pandas.errors import PerformanceWarning

# Suppress performance warnings from multi-index issues
warnings.filterwarnings("ignore", category=PerformanceWarning)

param = sys.argv[1]
start = dt.datetime(2017,1,1)
end = dt.datetime.now()

# Download stock data from Yahoo Finance using yfinance
df = yf.download(param, start, end)
data = df[["High", "Low", "Open", "Close"]]

#set our Linear Regression Model
model = LinearRegression()

while True:
    cmd = input("Enter Command: ")
    # Command to show the stock data plot for a specific part (High, Low, Open, Close)
    if cmd.lower() == "show stock":
        try:
            cmd = input("Which Part: ")
            df[cmd].plot()
            fig = plt.show(block=False)
            pass
        except:
            pass
    # Command to predict future stock prices
    if cmd.lower() == "predict":
        days = input("Enter Amount of days to predict: ")
        cmd = input("High, Low, Open, or Close: ")
        try:
            X = np.array(data.drop(cmd, axis=1))
            Y = np.array(data[cmd])
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
            model.fit(x_train, y_train)
        except:
            pass
        X_new = X[-50:]
        pred = model.predict(X_new[:int(days)])
        print(pred)
