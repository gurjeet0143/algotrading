# algotrading
In This project, I am trying to implements a Moving Average Crossover Strategy for stock trading using Python with AI. 
The strategy generates buy/sell signals when a short-term moving average crosses a long-term moving average, and compares performance against a buy-and-hold strategy.
I have used two moving averages: short-term (e.g., 20-day SMA) and long-term (e.g., 50-day SMA).
Buy Signal → when short SMA crosses above long SMA (golden cross).
Sell Signal → when short SMA crosses below long SMA (death cross).
# first steps
Download stock data (NIFTY, RELIANCE, AAPL) using yfinance.
Compute SMA(20) & SMA(50).
Generate buy/sell signals.
Backtest on historical data.
Plot equity curve & performance metrics.
