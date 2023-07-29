import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import os

BASE_DIR = 'datasets/cryptocurrencies/'
files = os.listdir(BASE_DIR)
files = [BASE_DIR+file for file in files]

st.title("Financial Portfolio Analysis...")

cryptocurrencies = st.sidebar.radio('Select a cryptocurrencies', files)

df = pd.read_csv(cryptocurrencies)
if st.sidebar.checkbox("view raw data"):
    st.subheader(f'📅{cryptocurrencies} data')
    st.dataframe(df, use_container_width=True)

st.subheader("Cryptocurrencies opening")
fig1 = px.pie(df, 'Year', 'Open', title="cryptocurrencies graph for opening")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies closing")
fig1 = px.pie(df, 'Year', 'Close', title="cryptocurrencies graph for closing")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies high")
fig1 = px.pie(df, 'Year', 'High', title="cryptocurrencies graph for high")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies low")
fig1 = px.pie(df, 'Year', 'Low', title="cryptocurrencies graph for low")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies volume")
fig1 = px.pie(df,'Year','Volume', title="cryptocurrencies graph for volume")
st.plotly_chart(fig1, use_container_width=True)


st.subheader("Cryptocurrencies year")
year_count = df['Year'].value_counts()
fig1 = px.bar(year_count,year_count.index,year_count.values, title="Year count")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cryptocurrencies ytd gains")
fig1 = px.density_heatmap(df,'Year','YTD Gain', title="cryptocurrencies graph for ytd gains")
st.plotly_chart(fig1, use_container_width=True)
