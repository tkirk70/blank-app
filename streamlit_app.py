import streamlit as st
import pandas as pd
import pandas_ta as ta
import yfinance as yf

# Title
st.title("Stock Technical Analysis App")

# Get the stock ticker symbol from the user
ticker = st.text_input("Enter Stock Ticker Symbol", "AAPL")

# Fetch stock data
data = yf.download(ticker)

# Calculate technical indicators
data.ta.sma(length=20, append=True)
data.ta.rsi(length=14, append=True)
data.ta.macd(append=True)
data.ta.bbands(append=True)

# Display the data
st.write(data)

# Plot the indicators
st.subheader("SMA")
st.line_chart(data[["Close", "SMA_20"]])

st.subheader("RSI")
st.line_chart(data["RSI_14"])

st.subheader("MACD")
st.line_chart(data[["MACD_12_26_9", "MACDs_12_26_9"]])

st.subheader("Bollinger Bands")
st.line_chart(data[["Close", "BBL_5_2.0", "BBM_5_2.0", "BBU_5_2.0"]])
