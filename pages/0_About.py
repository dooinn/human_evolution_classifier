
import streamlit as st
import pandas as pd
import numpy as np
import pickle

from utils import user_input_features, display_prediction_images,get_wikipedia_summary

data_path = 'cleaned.csv'
data = pd.read_csv(data_path)


# Load the preprocessor and model
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)
    
with open('best_logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)



# Example usage


st.sidebar.write("### Enter the features:")

    # Use the imported function to get user input
input_df = user_input_features()






# Assuming the prediction process is done within this block
if st.sidebar.button('Predict'): 
    processed_input = preprocessor.transform(input_df)
    prediction = model.predict(processed_input)
    article_summary = get_wikipedia_summary(prediction[0])
    st.write(f'# {prediction[0]}')
    st.write(f'#### Description: {article_summary["extract"]}')
    st.write(f'Source: {article_summary["content_urls"]["desktop"]["page"]}')
    st.image(article_summary["originalimage"]["source"])
    display_prediction_images(prediction[0])
