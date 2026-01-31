import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer")
st.subheader("Analyze and visualize stock prices over time.")

col1, col2, col3 = st.columns(3)
with col1:
    tickerName = st.text_input("Enter stock ticker", "MSFT")
with col2:
    startDate = st.date_input("Start date", datetime.date(2025, 1, 1))
with col3:
    enDate = st.date_input("End date", datetime.date(2025, 12, 31))

ticker = yf.Ticker(tickerName)
ticker_data = ticker.history(start=startDate, end=enDate)

st.subheader(f"The raw day wise stock data- {tickerName}")
st.dataframe(ticker_data.head())

st.subheader("Closing Price Chart:")
st.line_chart(ticker_data['Close'])

st.subheader("Volume Chart:")
st.bar_chart(ticker_data['Volume'])