import streamlit as st

name = st.sidebar.text_input("Enter your name")
st.sidebar.text_input("enter email")
st.sidebar.selectbox("select your gender", ['male', 'female'])
st.sidebar.write("thank you")

st.markdown(f"# Welcome {name}")
st.markdown(f"### Hope you are well")
st.markdown("> would like to have something?")

with st.expander("show product description"):
    st.write("""
             1. RAM : 16 GB
             2. Chipset : M4
             3. Storage : 256 GB
             """)