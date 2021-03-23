import streamlit as st
import cv2
import numpy as np
import keras
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np 
from PIL import Image,ImageOps 
import base64

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""

main_bg = "sample.png"
main_bg_ext = "png"

def app():
	new_model = keras.models.load_model("haemorrhage_modelnorm.h5")
	st.title("Haemorrhage Detection")
	st.markdown(
		"""
		<style>
		.reportview-container {
		#background: url("https://th.bing.com/th/id/OIP._Jb22j8XhAX_a20L-dX33wHaHa?pid=ImgDet&w=1023&h=1024&rs=1");
 		background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
		background-size: cover;
		}
		</style>
		""", unsafe_allow_html=True) 
	st.markdown(hide_streamlit_style, unsafe_allow_html=True);
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
