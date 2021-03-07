import streamlit as st
from multiapp import MultiApp
from apps import home, app1,app2 # import your app modules here
from PIL import Image

hi=Image.open('radiographer.png')
st.set_page_config(page_title='MedAI',page_icon=hi)

page_bg_img = '''
<style>
body {
background-image: url("https://images.app.goo.gl/GExjjCnEo5WU3v3o66");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

app = MultiApp()
st.sidebar.title('Image Analysis')
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Haemorrhage Detection", app1.app)
app.add_app("Pneumonia Detection",app2.app)

# The main app
app.run()
