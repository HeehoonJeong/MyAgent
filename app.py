import streamlit as st


st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")

st.badge('New')

st.markdown("*Streamlit* is **really** ***cool***.")


page_1 = st.Page('page_1.py', title='page 1')
page_2 = st.Page('page_2.py', title='page 2')
page_3 = st.Page('page_3.py', title='page 3')

pages = st.navigation([page_1, page_2, page_3])

pages.run()
