import streamlit as st
import cv2
import numpy as np
import keras
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np 
from PIL import Image,ImageOps 

#hi=Image.open('068.png')
#st.set_page_config(page_title='MedAI',page_icon=hi)

#PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":"hi","layout":"centered"}
#st.set_page_config(**PAGE_CONFIG)

html = '''
<style>
body {
background-image: url("https://img.freepik.com/free-vector/white-elegant-texture-wallpaper_23-2148421854.jpg?size=626&ext=jpg&ga=GA1.2.145878890.1611360000");
background-size: cover;
}
</style>
'''
st.markdown(html, unsafe_allow_html=True)

def app():
	new_model = keras.models.load_model("haemorrhage_model.h5")
	st.title("Haemorrhage Detection")
	#st.markdown(html, unsafe_allow_html=True)

	uploaded_file_hem = st.file_uploader("Choose a image file", type=['png','jpg','jpeg'])
	if uploaded_file_hem is not None:
		image = Image.open(uploaded_file_hem)	
		size = (128,128)
		image1=image.resize(size)
		image1=ImageOps.grayscale(image1)
		x = np.asarray(image1)
		x = np.expand_dims(x, axis=0)
		x=np.reshape(x,(1,128,128,1))
		x=x/255.0
		if(new_model.predict_classes(x)[0][0]==1):
			st.write('***Haemorrhage***')
			if st.button('Show Image'):
				st.image(image,channels='BGR',width=300)
		else:
			st.write('***Normal***')
			if st.button('Show Image'):
				st.image(image,channels='BGR',width=300)
		
  			

#if __name__ == '__main__':
	#app(
