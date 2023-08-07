import streamlit as st
import qrcode
from PIL import Image

st.title("QR Code Generator")

data = st.text_input("Your text/data")

img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
img.save("_pic.png")

image = Image.open('_pic.png')  # Corrected file extension
st.image(image, caption='Your QR Code')
