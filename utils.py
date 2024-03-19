import streamlit as st
import pandas as pd
import os
from PIL import Image
import requests

def user_input_features():

    current_country = st.sidebar.selectbox('Current Country', ['Kenya', 'Republic of Chad', 'Germany', 'Ethiopia', 'Indonesia', 'South Africa', 'Georgia', 'Spain'])
    habitat = st.sidebar.selectbox('Habitat', ['forest-gallery', 'mixed', 'cold forest', 'forest', 'savannah', 'jungle', 'all', 'peninsular', 'forest-savanna']) 
    
    cranial_capacity = st.sidebar.number_input('Cranial Capacity (cc)', min_value=50.0, max_value=2000.0, value=400.0)

    jaw_shape = st.sidebar.selectbox('Jaw Shape', ['U shape', 'conical', 'modern', 'V shape', 'very modern'])

    prognathism = st.sidebar.selectbox('Prognathism', ['very high','high','medium-high','medium','reduced','very reduced','absent'])

    height = st.sidebar.number_input('Height (cm)', min_value=50.0, max_value=250.0, value=160.0)
    skeleton = st.sidebar.selectbox('Skeleton', ['light','refined','robust'])

    hip = st.sidebar.selectbox('Hip', ['wide', 'slim', 'very modern', 'modern']) 
    foots = st.sidebar.selectbox('Foots', ['climbing', 'walk'])
    biped = st.sidebar.selectbox('Biped', ['low probability','high probability','yes','modern'])  
    arms = st.sidebar.selectbox('Arms', ['climbing','manipulate','manipulate with precision'])
    
    sexual_dimorphism = st.sidebar.selectbox('Sexual Dimorphism', ['reduced','medium-high','high']) 
    

    diet = st.sidebar.selectbox('Diet', ['dry fruits', 'carnivorous', 'hard fruits', 'omnivore', 'soft fruits'])

    data = {
        'cranial_capacity': [cranial_capacity],
        'height': [height],
        'current_country': [current_country],
        'habitat': [habitat],
        'jaw_shape': [jaw_shape],
        'foots': [foots],
        'diet': [diet],
        'hip': [hip],
        'prognathism': [prognathism],
        'biped': [biped],
        'arms': [arms],
        'sexual_dimorphism': [sexual_dimorphism],
        'skeleton': [skeleton]
    }
    features = pd.DataFrame(data)
    return features



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



def get_wikipedia_summary(title):
    """
    Fetches the summary of a Wikipedia article by title.
    
    Args:
    - title (str): The title of the Wikipedia article.
    
    Returns:
    - dict: A dictionary containing the summary and other metadata.
    """
    # Define the URL for the Wikipedia API
    URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    
    # Make a GET request to fetch the article summary
    response = requests.get(URL + title)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response content
        return response.json()
    else:
        return {"error": "Article not found or API request failed."}

