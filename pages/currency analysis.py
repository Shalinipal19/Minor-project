import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import os

BASE_DIR = 'datasets/currencies/'
files = os.listdir(BASE_DIR)
files = [BASE_DIR+file for file in files]

st.title("Project title")

currencies = st.sidebar.radio('Select a currencies', files)

df = pd.read_csv(currencies)
if st.sidebar.checkbox("view raw data"):
    st.subheader(f'📅{currencies} data')
    st.dataframe(df)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

period = st.radio('Select time period sample', ['D','W',"M",'Y'], horizontal=True)

st.subheader("Currencies openining")
dfopen = df.resample(period)['Open'].sum()
fig1 = px.line(dfopen, dfopen.index, 'Open', title="currencies graph for opening")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies closing")
dfclose = df.resample(period)['Close'].sum()
fig1 = px.line(dfclose, dfclose.index, 'Close', title="currencies graph for closing")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies high")
dfhigh = df.resample(period)['High'].sum()
fig1 = px.line(dfhigh, dfhigh.index, 'High', title="currencies graph for high")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies low")
dflow = df.resample(period)['Low'].sum()
fig1 = px.line(dflow, dflow.index, 'Low', title="currencies graph for low")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies ytd gains")
dfytdgains = df.resample(period)['YTD Gains'].sum()
fig1 = px.line(dfytdgains, dfytdgains.index, 'YTD Gains', title="currencies graph for ytd gains")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies volume")
dfvolume = df.resample(period)['Volume'].sum()
fig1 = px.line(dfvolume, dfvolume.index, 'Volume', title="currencies graph for volume")
st.plotly_chart(fig1, use_container_width=True)


