import streamlit as st
from PIL import Image
from img_classification import teachable_machine_classification
import requests

st.title("Image Classification with Google's Teachable Machine")
st.header("Breast Cancer Ultrasound Classification Example")
st.text("Upload a scan for Classification")

# Di dalam kode Anda yang mengunggah dan memproses gambar
uploaded_file = st.file_uploader("Choose a scan ...", type={"png", "jpg", "jpeg"})
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Scan.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'model/keras_model.h5')
    if label == 0:
        st.write("The scan is normal")
    elif label == 1:
        st.write("The scan is malignant")
    else: 
        st.write("The scan is benign")
