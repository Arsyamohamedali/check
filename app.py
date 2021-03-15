import streamlit as st
from multiapp import MultiApp
from apps import home, app1,app2 # import your app modules here
from PIL import Image

hi=Image.open('radiographer.png')
st.set_page_config(page_title='MedAI',page_icon=hi)

st.markdown(
    '''
    <style>
    .html {
    background-image: url("https://img.freepik.com/free-vector/white-elegant-texture-wallpaper_23-2148421854.jpg?size=626&ext=jpg&ga=GA1.2.145878890.1611360000");
    background-size: cover;
    }
    </style>
    ''', 
    unsafe_allow_html=True)

app = MultiApp()
st.sidebar.title('Image Analysis')
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Haemorrhage Detection", app1.app)
app.add_app("Pneumonia Detection",app2.app)

# The main app
app.run()
