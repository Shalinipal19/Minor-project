import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import os

BASE_DIR = 'datasets/currencies/'
files = os.listdir(BASE_DIR)
files = [BASE_DIR+file for file in files]

st.title("Financial portfolio analysis")

currencies = st.sidebar.radio('Select a currencies', files)

df = pd.read_csv(currencies)
if st.sidebar.checkbox("view raw data"):
    st.subheader(f'📅{currencies} data')
    st.dataframe(df, use_container_width=True)

st.subheader("Currencies opening")
fig1 = px.pie(df, 'Year', 'Open', title="currencies graph for opening")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies closing")
fig1 = px.pie(df, 'Year', 'Close', title="currencies graph for closing")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies high")
fig1 = px.bar(df, 'Year', 'High', title="currencies graph for high")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Currencies low")
fig1 = px.bar(df, 'Year', 'Low', title="currencies graph for low")
st.plotly_chart(fig1, use_container_width=True)




st.subheader("Currencies ytd gains")
fig1 = px.bar(df,'Year','YTD Gain', title="currencies graph for ytd gains")
st.plotly_chart(fig1, use_container_width=True)



