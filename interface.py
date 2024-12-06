import streamlit as st
import pandas as pd
import textenc.aesctr as aesct
import imageenc.torgb as torgb
from imageenc.rsaimage import ImageEncryptor
import textenc.rsa as rsa



imageEncryptor = ImageEncryptor()
image1 = st.file_uploader("Upload first file")
image2 = st.file_uploader("Upload the second file")
st.image(imageEncryptor.temp(image1, image2))
st.image(torgb.imagetest())
rsa = rsa.RSAtext()
print(rsa)
print("Test")
st.title("A :blue[Composite] Scoring Algorithm for Combinations of Steganography, Encryption, and File Compression in Real World Environments")

with st.sidebar:
    st.title("Dependencies")
    security = st.slider("How important is :blue[security?]")
    secrecy = st.slider("How important is secrecy?")
    bandwidth = st.slider("How important is bandwidth management?")
    file_type = st.segmented_control("What kinds of files are relevant?", ["Text", "Images", "Videos"])
    


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [security, secrecy, bandwidth]
}))
