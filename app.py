import streamlit as st
from predict_page import predict_pg
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    predict_pg()
else:
    show_explore_page()