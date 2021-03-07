import streamlit as st
from multiapp import MultiApp
from apps import home, app1,app2 # import your app modules here
from PIL import Image

hi=Image.open('radiographer.png')
st.set_page_config(page_title='MedAI',page_icon=hi)

page_bg_img = '''
<style>
body {
background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=DOpvGm59&id=BD3DCDE8B890223A653ADDEE453006E6F3D386F8&thid=OIP.DOpvGm59LDFpAPtBJbZHxQHaEN&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR0cea6f1a6e7d2c316900fb4125b647c5%3frik%3d%252bIbT8%252bYGMEXu3Q%26riu%3dhttp%253a%252f%252fblogs.adobe.com%252fdreamweaver%252ffiles%252f2015%252f06%252fraindrops-nofilter.png%26ehk%3dyOpNYn9dO6g091p1MMusMF8PZEhf62C%252fFOJ%252bHlIyrgw%253d%26risl%3d%26pid%3dImgRaw&exph=504&expw=885&q=background+image+in+css&simid=608018248520435533&ck=0DD6959C21ADB7013E62BCFC23087ECC&selectedIndex=24&FORM=IRPRST");
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
