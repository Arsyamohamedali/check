import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
from PIL import Image
import base64

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""

main_bg = "sample1.png"
main_bg_ext = "png"

def app(): 
    st.markdown(
	f"""
	<style>
	.reportview-container {{
		#background: url("https://th.bing.com/th/id/OIP._Jb22j8XhAX_a20L-dX33wHaHa?pid=ImgDet&w=1023&h=1024&rs=1");
 	background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
	background-size: cover;
	}}
	</style>
	""", unsafe_allow_html=True) 
    st.markdown(hide_streamlit_style, unsafe_allow_html=True);
    


    LOGO_IMAGE = "radiographer.png"

    st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:100px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
        margin-left:auto;
    }
    .logo-img {
        float:right;
        width:300px;
        height:300px;
        # margin-left:auto;
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
        font-weight:bold;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown('<p class="bigg-font">Need Medical Assistance??</p>', unsafe_allow_html=True)

    st.write("***Here's the solution***")
    st.write("This portal can help you with medical solutions!!")

    st.button('← Check It Out')
      


