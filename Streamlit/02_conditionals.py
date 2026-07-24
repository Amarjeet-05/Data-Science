import streamlit as st

# we learnt about different kind of selection
# checkbox, selectbox, radio, number_input, text_input, button

st.title("About order")
add = "would you like to add:" #here this message we are using for each product so we are storing it to the variable so in future if we want to change in message we can easily change at once instead changing on each products
qty = "qty"
min = 1
max = 3

products = ["laptop", "mobile", "computer", "smart watch", "tablets"]
main_product = st.selectbox("select your product:", products, index=None, placeholder="add item") #index=None will remove by default selection of the element

if main_product in products:
    color = st.radio("Pick which color you want: ", ['Black', 'White', 'Grey', 'Sky'])



if main_product == "laptop":
    st.number_input(qty, min_value = min, max_value= max)
    st.write(add)
    st.checkbox("Bag")
    st.checkbox("Keyboard")
    st.checkbox("mouse")

# or

if main_product == "mobile": 
    st.number_input(qty, min_value= min, max_value= max)
    st.write(add)
    cov, tem, ada = st.columns(3)
    with cov:
        st.checkbox("Cover")
    with tem:
        st.checkbox("Tempered Glass")
    with ada:
        st.checkbox("Adapter")


if main_product == "computer":
    st.number_input(qty, min_value= min, max_value= max)

    st.write(add)
    mou, key, cab, mon = st.columns(4)

    with mou: 
        st.checkbox("mouse")
    with key: 
        st.checkbox("keyboard")
    with cab: 
        st.checkbox("cabinate")
    with mon: 
        st.checkbox("monitor")

if main_product == "smart watch": 
    st.number_input(qty, min_value= min, max_value= max)

    st.write(add)
    stra, mem = st.columns(2)
    with stra:
        st.checkbox("stapes")
    with mem:
        st.checkbox("membrane")


name = st.text_input("enter your name")

    
if main_product in products:
    if st.button("place order"): 
        st.success(f"{name} you ordered successfully!")
