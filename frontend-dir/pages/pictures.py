import streamlit as st
from PIL import Image
import os.path

st.title("Pictures")

####### PICTURE OF ZED ########
image =Image.open("/app/frontend-dir/league-of-legends/zed.png")
st.image(image, caption='Shockblade Zed')
st.button("Download")

####### PICTURE OF THRESH ########
image =Image.open("/app/frontend-dir/league-of-legends/thresh.jpg")
st.image(image, caption='Thresh')
st.button("Download")


####### PICTURE OF TEEMO ########
image =Image.open("/app/frontend-dir/league-of-legends/teemo.jpeg")
st.image(image, caption='Teemo')
st.button("Download")

####### PICTURE OF LOL ########
image =Image.open("/app/frontend-dir/league-of-legends/teemo.jpeg")
st.image(image, caption='League Of Legends')
st.button("Download")