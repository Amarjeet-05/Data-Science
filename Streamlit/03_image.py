import streamlit as st


st.title("About order")
add = "would you like to add:"
qty = "qty"
min = 1
max = 3

products = ["laptop", "mobile", "computer", "smart watch", "tablets"]
main_product = st.selectbox("select your product:", products, index=None, placeholder="add item")


if main_product in products:
    color = st.radio("Pick which color you want: ", ['Black', 'White', 'Sky'])



if main_product == "laptop":
    if color == 'Black':
        img1, img2, img3 = st.columns(3)
        with img1:
            st.image("https://media.tatacroma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/318776_1_D4-_EpGsp.png?updatedAt=1772623949676", width=200)
        with img2:
            st.image("https://media-ik.croma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/310949_0_dn1klv.png", width=200)
        with img3:
            st.image("https://media.tatacroma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/302746_5_cfxbvn.png", width=200)

    if color == "White":
        img1, img2, img3 = st.columns(3)
        with img1: 
            st.image("https://media.tatacroma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/302725_4_wb4lqx.png", width = 200)
        with img2:
            st.image("https://media-ik.croma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/310946_0_nulnul.png", width = 200)
        with img3:
            st.image("https://media.tatacroma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/302725_5_buzjaq.png", width=200)
    
    if color == "Sky":
        img1, img2, img3 = st.columns(3)
        with img1:
            st.image("https://media-ik.croma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/324360_0_0l1Y9j1w3.png?updatedAt=1782721114085", width=200)
        with img2:
            st.image("https://media.tatacroma.com/Croma%20Assets/Computers%20Peripherals/Laptop/Images/314064_7_ubgge3.png", width=200)
        with img3:
            st.image("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202604/apple-macbook-air-m5-09390442-1x1.jpg?VersionId=FP6LzqtUWy2lyYh9RtUL96a3fPcmLeCe", width=200)
    
    st.number_input(qty, min_value = min, max_value= max)
    st.write(add)
    st.checkbox("Bag")
    st.checkbox("Keyboard")
    st.checkbox("mouse")

# or

if main_product == "mobile": 
    if color == "Black":
        st.image("https://media-ik.croma.com/Croma%20Assets/Communication/Mobiles/Images/309725_0_fk5km3.png", width=500)
    
    if color == "White":
        st.image("https://media-ik.croma.com/Croma%20Assets/Communication/Mobiles/Images/300748_0_g45gih.png", width=500)
    
    if color == "Sky": 
        st.image("https://media-ik.croma.com/Croma%20Assets/Communication/Mobiles/Images/243516_0_yxck9x.png", width = 500)
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
        st.write("please share your feedback")
        sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
        stars = st.feedback("stars")
        if stars is not None:
            st.markdown(f"You selected star(s).")



