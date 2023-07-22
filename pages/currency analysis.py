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
