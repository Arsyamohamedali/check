import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Haemorrhage Detection", app1.py)
app.add_app("Pneumonia Detection",app2.py)

# The main app
app.run()
