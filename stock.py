import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import os

BASE_DIR = 'datasets/stocks/'
files = os.listdir(BASE_DIR)
files = [BASE_DIR+file for file in files]
st.image('hero.jpg',use_column_width=True)
st.title("Financial Portfolio Analysis..") 

stock = st.sidebar.radio('Select a stock', files)

df = pd.read_csv(stock)
if st.sidebar.checkbox("view raw data"):
    st.subheader(f'📅{stock} data')
    st.dataframe(df, use_container_width=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

period = st.radio('Select time period sample', ['D','W',"M",'Y'], horizontal=True)

st.subheader("Stock openining")
dfopen = df.resample(period)['Open'].sum()
fig1 = px.line(dfopen, dfopen.index, 'Open', title="stocks graph for opening")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Stock closing")
dfclose = df.resample(period)['Close'].sum()    
fig1 = px.line(dfclose, dfclose.index, 'Close', title="stocks graph for closing")
st.plotly_chart(fig1, use_container_width=True)


st.subheader("Stock high")
dfhigh = df.resample(period)['High'].sum()    
fig1 = px.line(dfhigh, dfhigh.index, 'High', title="stocks graph for high")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Stock low")
dflow = df.resample(period)['Low'].sum()    
fig1 = px.line(dflow, dflow.index, 'Low', title="stocks graph for low")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Stock volume")
dfvolume = df.resample(period)['Volume'].sum()    
fig1 = px.line(dfvolume, dfvolume.index, 'Volume', title="stocks graph for volume")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Stock ytd gains")
dfytdgains= df.resample(period)['YTD Gains'].sum()    
fig1 = px.line(dfytdgains, dfytdgains.index, 'YTD Gains', title="stocks graph for ytd gains")
st.plotly_chart(fig1, use_container_width=True)
