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
    background-image: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/rm21-background-tong-058.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=710a6fed5b1923da8d5f95191839ef8a");
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
