import streamlit as st
from PIL import Image
import os.path

st.title("Pictures - Credits to wallpapercave.com")
new_height = 720

####### PICTURE OF ZED ########
image =Image.open("/app/frontend-dir/league-of-legends/zed3.jpg")
# resizing the image to 720p
new_width = int(new_height / image.height *image.width)
image.resize((new_width, new_height))
st.image(image, caption='Zed')
st.button("Download", key="1")

####### PICTURE OF POPPY ########
image =Image.open("/app/frontend-dir/league-of-legends/poppy.png")
# resizing the image to 720p
new_width = int(new_height / image.height *image.width)
image.resize((new_width, new_height))
st.image(image, caption='Poppy')
st.button("Download", key="2")


####### PICTURE OF VI AND JINX ########
image =Image.open("/app/frontend-dir/league-of-legends/vi-jinx.png")
# resizing the image to 720p
new_width = int(new_height / image.height *image.width)
image.resize((new_width, new_height))
st.image(image, caption='Jinx-Vi')
st.button("Download", key="3")

####### PICTURE OF MASTER YI ########
image =Image.open("/app/frontend-dir/league-of-legends/master-yi.png")
# resizing the image to 720p
new_width = int(new_height / image.height *image.width)
image.resize((new_width, new_height))
st.image(image, caption='Master Yi')
st.button("Download", key="4")

####### PICTURE OF KARTHUS ########
image =Image.open("/app/frontend-dir/league-of-legends/karthus.png")
# resizing the image to 720p
new_width = int(new_height / image.height *image.width)
image.resize((new_width, new_height))
st.image(image, caption='Karthus')
st.button("Download", key="5")