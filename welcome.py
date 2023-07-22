import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import os

BASE_DIR = 'datasets/stocks/'
files = os.listdir(BASE_DIR)
files = [BASE_DIR+file for file in files]

st.title("Project title")

stock = st.sidebar.radio('Select a stock', files)

df = pd.read_csv(stock)
if st.sidebar.checkbox("view raw data"):
    st.subheader(f'📅{stock} data')
    st.dataframe(df)



