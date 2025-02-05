import pandas as pd
import yfinance as yf

def get_finance_df(days: int, tickers: dict[str, str]):
    cat_hist = pd.DataFrame()
    for company_name, company_a in tickers.items():
        ticker = yf.Ticker(company_a)
        hist = ticker.history(period=f"{days}d")
        hist.index = hist.index.strftime("%d %B %Y")
        hist = hist[["Close"]]
        hist.columns = [company_name]
        hist = hist.T
        hist.index.name = "Name"
        cat_hist = pd.concat((cat_hist, hist))
    return cat_hist


