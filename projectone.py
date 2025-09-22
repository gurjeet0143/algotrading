# Step 1: Install dependencies (run this once in your environment)
# pip install yfinance pandas matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Download Stock Data (Example: RELIANCE or AAPL)
ticker = "RELIANCE.NS"   # NSE stock; use "AAPL" for Apple, "MSFT" for Microsoft
data = yf.download(ticker, start="2020-01-01", end="2025-01-01")

# Check if data is downloaded
if data.empty:
    print("No data found for the ticker. Please check the ticker symbol or your internet connection.")
    exit()

# Step 3: Calculate Short-term and Long-term Moving Averages
data['SMA20'] = data['Close'].rolling(window=20, min_periods=1).mean()   # short-term
data['SMA50'] = data['Close'].rolling(window=50, min_periods=1).mean()   # long-term

# Step 4: Generate Buy/Sell Signals
data['Signal'] = 0
data['Signal'] = (data['SMA20'] > data['SMA50']).astype(int)

# Step 5: Create Position Column (1 = Buy, -1 = Sell, 0 = Hold)
data['Position'] = data['Signal'].diff().fillna(0)

# Step 6: Plot Strategy
plt.figure(figsize=(14,7))
plt.plot(data.index, data['Close'], label='Price', alpha=0.6)
plt.plot(data.index, data['SMA20'], label='SMA20', alpha=0.8)
plt.plot(data.index, data['SMA50'], label='SMA50', alpha=0.8)

# Buy signals
plt.plot(data[data['Position'] == 1].index,
         data['SMA20'][data['Position'] == 1],
         '^', markersize=12, color='g', label='Buy Signal')

# Sell signals
plt.plot(data[data['Position'] == -1].index,
         data['SMA20'][data['Position'] == -1],
         'v', markersize=12, color='r', label='Sell Signal')

plt.title(f"{ticker} - Moving Average Crossover Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Step 7: Backtest Strategy
# Daily returns
data['Return'] = data['Close'].pct_change().fillna(0)

# Strategy returns (when Signal=1, invest in stock; else stay in cash)
data['Strategy_Return'] = data['Signal'].shift(1).fillna(0) * data['Return']

# Step 8: Calculate Performance
cumulative_stock = (1 + data['Return']).cumprod()
cumulative_strategy = (1 + data['Strategy_Return']).cumprod()

plt.figure(figsize=(14,7))
plt.plot(data.index, cumulative_stock, label="Buy & Hold")
plt.plot(data.index, cumulative_strategy, label="Strategy")
plt.title("Strategy vs Buy & Hold")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Final Returns
print("Final Buy & Hold Return:", round(cumulative_stock.iloc[-1], 2))
print("Final Strategy Return:", round(cumulative_strategy.iloc[-1], 2))