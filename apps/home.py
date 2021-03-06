import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

def app():
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-color:'red';
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
