import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

def app():
    page_bg_img = '''
    <style>
    body {
        background-image: url("https://images.app.goo.gl/usCdWH5UYSp2UpCAA");
        background-size: cover;
    }
    </style>
    '''

st.markdown(page_bg_img, unsafe_allow_html=True)
        
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        color:#02346;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">MedAI</p>', unsafe_allow_html=True)
    #st.title('MedAI')
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

    st.write("This is HomePage.")
    #st.markdown("### Sample Data")
    #df = create_table()
    #st.write(df)

    #st.write('Navigate to `Data Stats` page to visualize the data')
