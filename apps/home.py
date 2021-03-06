import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
from PIL import Image
import base64

def app():  
    LOGO_IMAGE = "radiographer.png"

    st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
        width:500px;
        height:500px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">MedAI </p>
    </div>
    """,
    unsafe_allow_html=True
    )

    
    st.markdown("""
    <style>
    .bigg-font {
        font-size:50px !important;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown('<p class="bigg-font">Medical Problem??</p>', unsafe_allow_html=True)

    st.write("***Here's the solution***")
    st.write("This portal cn help you with medical solutions!!")
    #st.markdown("### Sample Data")
    #df = create_table()
    #st.write(df)

    #st.write('Navigate to `Data Stats` page to visualize the data')
