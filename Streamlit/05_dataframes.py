import streamlit as st
import pandas as pd

# we can do more pandas and datavisualization operations

file = st.file_uploader("uplaod you file", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("preview of the dataset")
    st.dataframe(df)

if file:
    st.title("summary stats")
    st.write(df.describe())

if file:
    cities = df['city'].unique()
    st.subheader("filter data city wise: ")
    selected_city = st.selectbox("select a city ",cities, index=None)
    st.dataframe(df[df['city'] == selected_city])

