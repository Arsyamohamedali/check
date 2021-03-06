import streamlit as st
from multiapp import MultiApp
from apps import home, app1,app2 # import your app modules here

app = MultiApp()
st.sidebar.title('Image Analysis')
# Add all your application here
app.add_app("MedAI", home.app)
app.add_app("Haemorrhage Detection", app1.app)
app.add_app("Pneumonia Detection",app2.app)

# The main app
app.run()
