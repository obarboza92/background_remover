from rembg import remove
from PIL import Image
import streamlit as st
import io

st.title("Background Remover Demo")
col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Carga la imagen deseada", accept_multiple_files =True)
if images:
    for image in images:
        try:
            with Image.open(image) as img:
                col1.header("Original")
                col1.image(img)

                output = remove(img)
                col2.header("Extracted")
                col2.image(output)

                # Convert the image to a byte array with format information
                output_buffer = io.BytesIO()
                output.save(output_buffer, format="PNG")

                # Download button triggers download immediately (no inner if statement)
                col2.download_button(
                    label="Descargar imagen recortada",
                    data=output_buffer.getvalue(),
                    file_name=f"{image.name.split('.')[0]}_no_background.png",
                    mime="image/png"
                )            
        except Exception as e:
            col2.error(f"Error al intentar remover el fondo de la imagen: {e}")
            continue  # Skip to the next image if there's an error
st.info("Presione el boton de descarga para descargar la imagen recortada.")