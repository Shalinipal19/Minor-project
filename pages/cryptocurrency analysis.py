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
    st.dataframe(df)
