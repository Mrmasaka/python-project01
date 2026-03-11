import yfinance as yf
import pandas as pd

tickers = ["SPY", "QQQ", "VTI"]

for ticker in tickers:
    data = yf.download(
        ticker,
        period="1y",
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    print(f"Downloaded {ticker}")
    print(data.head())

    data.to_csv(f"data/{ticker.lower()}.csv")
    print(f"Saved to data/{ticker.lower()}.csv")