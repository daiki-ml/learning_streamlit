import streamlit as st
import time
import pandas as pd
# import matplotlib.pyplot as plt
import yfinance as yf

from get_finance import get_finance_df

st.title("米国TOP企業の株価")

tickers = {
    "apple": "AAPL",
    "meta": "META",
    "google": "GOOGL",
    "microsoft": "MSFT",
    "netflix": "NFLX",
    "amazon": "AMZN"
}
hist = get_finance_df(20, tickers)
st.write(hist)