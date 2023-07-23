import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import os

BASE_DIR = 'datasets/cryptocurrencies/'
files = os.listdir(BASE_DIR)
files = [BASE_DIR+file for file in files]

st.title("Project title")

cryptocurrencies = st.sidebar.radio('Select a cryptocurrencies', files)

df = pd.read_csv(cryptocurrencies)
if st.sidebar.checkbox("view raw data"):
    st.subheader(f'📅{cryptocurrencies} data')
    st.dataframe(df, use_container_width=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

period = st.radio('Select time period sample', ['D','W',"M",'Y'], horizontal=True)

st.subheader("Cryptocurrencies openining")
dfopen = df.resample(period)['Open'].sum()
fig1 = px.line(dfopen, dfopen.index, 'Open', title="cryptocurrencies graph for opening")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies closing")
dfclose = df.resample(period)['Close'].sum()
fig1 = px.line(dfclose, dfclose.index, 'Close', title="cryptocurrencies graph for closing")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies high")
dfhigh = df.resample(period)['High'].sum()
fig1 = px.line(dfhigh, dfhigh.index, 'High', title="cryptocurrencies graph for high")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies low")
dflow = df.resample(period)['Low'].sum()
fig1 = px.line(dflow, dflow.index, 'Low', title="cryptocurrencies graph for low")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies ytd gains")
dfytdgains = df.resample(period)['YTD Gains'].sum()
fig1 = px.line(dfytdgains, dfytdgains.index, 'YTD Gains', title="cryptocurrencies graph for ytd gains")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies volume")
dfvolume = df.resample(period)['Volume'].sum()
fig1 = px.line(dfvolume, dfvolume.index, 'Volume', title="cryptocurrencies graph for volume")
st.plotly_chart(fig1, use_container_width=True)

