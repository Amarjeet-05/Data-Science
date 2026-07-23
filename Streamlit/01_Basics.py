import streamlit as st 
# here we are using uv (in terminal) which does not require manually installing libraries and creating virtual environment 

st.title("This is the title")
st.subheader("this is the subheader")
st.text("hello")

st.write("how are you") #we can use it like our print statement

selection = st.selectbox("select products",  ["laptops", "mobiles", "Computers", "headphones", "charger"])

st.write(f"you selected {selection}")


st.success(f"you device ({selection}) selected successfully!")