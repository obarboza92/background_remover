from rembg import remove
from PIL import Image
import streamlit as st

st.title("Background Remover Demo")
col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Cargue la imagen deseada", accept_multiple_files =True)
if images:
    for image in images:
        with Image.open(image) as img:
            col1.header("Original")
            col1.image(img)

            output = remove(img)
            col2.header("Extracted")
            col2.image(output)
            