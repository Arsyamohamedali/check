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

#html = '''
#<style>
#body {
#background-image: url("https://img.freepik.com/free-vector/white-elegant-texture-wallpaper_23-2148421854.jpg?size=626&ext=jpg&ga=GA1.2.145878890.1611360000");
#background-size: cover;
#}
#</style>
#'''

def app():
	new_model = keras.models.load_model("modelPN.h5")
	st.title("Pneumonia Detection")
	#st.markdown(html, unsafe_allow_html=True)
	
	uploaded_file = st.file_uploader("Choose a image file", type=['png','jpg','jpeg'])
	if uploaded_file is not None:
		image = Image.open(uploaded_file)	
		#st.image(image,channels='BGR')
		
	
	#images = image.load_img(img, target_size=(150,150))    
	#x = image.img_to_array(images)
	#x = tf.image.rgb_to_grayscale(x)
	#x = np.expand_dims(x, axis=0)
	#x = x/255.0
		size = (150,150)
	#image1 = ImageOps.fit(img, size, Image.ANTIALIAS)
		image1=image.resize(size)
		image1=ImageOps.grayscale(image1)
		x = np.asarray(image1)
		x = np.expand_dims(x, axis=0)
		x=np.reshape(x,(-1,150,150,1))
		x=x/255.0
		if(new_model.predict_classes(x)[0][0] == 1):
			st.write('***Normal***')
			if st.checkbox('checkbox'):
				st.image(image,channels='BGR')
		else:
  			st.write('***Pneumonia***')
			
			if st.checkbox('checkbox'):
				st.image(image,channels='BGR')
#if __name__ == '__main__':
	#app()
