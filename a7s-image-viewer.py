import streamlit as st
from PIL import Image, UnidentifiedImageError
import imageio.v2 as imageio  # Use the v2 version of imageio
import numpy as np

st.set_page_config(page_title="A7's Image Viewer", page_icon="🖼️", layout="wide")

st.markdown("""
<style>
    .main {
        background-color: #f0f2f5;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    h1, h2 {
        color: #333;
    }
    .img-container {
        border-radius: 10px;
        overflow: hidden;
        transition: transform 0.2s;
    }
    .img-container:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

st.title("A7's Image Viewer")
st.write("Upload and view your Images in style!")


st.sidebar.header("Upload Images")
uploaded_files = st.sidebar.file_uploader(
    "Choose images", 
type = [
    "apng", "bmp", "cur", "dds", "dng", 
    "dib", "fits", "gif", "jpeg", "jfif", 
    "jpg", "pcd", "pcx", "png", "psd", 
    "qoi", "tiff", "webp", "sgi", 
    "xbm", "tga", "pbm", "pgm", "ppm", 
    "pnm", "jps", "fts", "ras", "jp2", 
    "fit"
        ],



    accept_multiple_files=True
)

# Display uploaded images
if uploaded_files:
    st.write("## Gallery")
    cols = st.columns(3)  
    for i, uploaded_file in enumerate(uploaded_files):
        try:
            uploaded_file.seek(0)  
            image = Image.open(uploaded_file)
            with cols[i % 3]:  
                st.markdown('<div class="img-container">', unsafe_allow_html=True)
                if image.format == 'GIF':
                    # Use Streamlit's st.image directly for GIFs to allow animation
                    st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)
                else:
                    st.image(image, caption=uploaded_file.name, use_column_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

        except UnidentifiedImageError:
            st.error(f"This image format is not supported {uploaded_file.name}. Please upload a valid image file.")
        except Exception as e:
            st.error(f"An error occurred while processing {uploaded_file.name}: {e}")
else:
    st.info("Please upload images to view them.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Made by A7 Nostalgic under A7's Garage")
st.sidebar.write("Any Bugs or Suggestions")
st.sidebar.write("Feel free to reach out at: [a7sgarage@gmail.com](mailto:a7sgarage@gmail.com)\n\n [patnamkannabhiram@gmail.com](mailto:patnamkannabhiram@gmail.com)")

