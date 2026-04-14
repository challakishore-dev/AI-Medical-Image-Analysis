import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import numpy as np
from PIL import Image
from src.predict import predict_image_array

st.title("Medical Image AI")

file = st.file_uploader("Upload Image")

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    result = predict_image_array(np.array(img))

    st.subheader("Prediction Result")
    st.success(f"Prediction: {result}")
