import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
from PIL import Image

def app():    
    img=Image.open("radiographer.png")
    st.image(img,width=200)
    st.markdown("""
    <style>
    .big-font {
        font-size:35px !important;
        color:#02346;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">MedAI</p>', unsafe_allow_html=True)
    #st.title('MedAI')
    
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
