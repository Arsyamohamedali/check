import streamlit as st
import cv2
import numpy as np
import keras
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np 
from PIL import Image,ImageOps 


def app():
	new_model = keras.models.load_model("haemorrhage_modelnorm.h5")
	st.title("Haemorrhage Detection")
	page_bg_img = '''
	<style>
	body {
	background-image: url("https://i1.wp.com/static.web-backgrounds.net/uploads/2012/08/City_Landscape_Background.jpg");
	background-size: cover;
	}
	</style>
	'''
	
	st.markdown(page_bg_img, unsafe_allow_html=True)

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
