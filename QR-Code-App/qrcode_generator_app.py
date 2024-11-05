import streamlit as st
import segno
import time

st.set_page_config(page_title="My QR Code App",
                   page_icon=":white_check_mark:")

# add a banner
st.image("https://library-images.kamiapp.com/library/_next/image?url=https:%2F%2Fstorage.googleapis.com%2Fkami-uploads-public%2Flibrary-resource-egxYhSV74CxA-vdSy9m-google-classroom-banner-paint-splats-png&w=3840&q=75")

# add a title
st.title("QR CODE GENERATOR")

# create an input box and store the input in a variable
url = st.text_input("Enter the data you would like to encode")

color = st.color_picker("Pick a Color for QR Code")

button = st.button("Click Here to Generate QR Code")

st.write(url)

def generate_qrcode(url, color):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark="white",
                  light=color).save()

# if something is input
if url and button:
    with st.spinner("generating  QR code"):
        time.sleep(1)
    generate_qrcode(url, color)
    st.image("images/qrcode_streamlit.png",
             caption="My QR CODE")

