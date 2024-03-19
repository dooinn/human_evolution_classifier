import streamlit as st
import os
from PIL import Image


def display_prediction_images(prediction):
    # Format the prediction result to match the image filenames
    formatted_prediction = prediction.lower().replace(" ", "_")
    
    # Construct the path to the images folder
    images_folder = 'images'
    
    # Supported image extensions
    supported_extensions = ['jpg', 'jpeg', 'webp']
    
    # Find all images for the predicted species with supported extensions
    image_files = [f for f in os.listdir(images_folder) if f.startswith(formatted_prediction) and f.split('.')[-1] in supported_extensions]
    
    if image_files:

        for image_file in image_files:
            image_path = os.path.join(images_folder, image_file)
            image = Image.open(image_path)
            # Display each image with a caption
            st.image(image, caption=image_file, use_column_width=True)
    else:
        st.write("No images found for the predicted species.")
