
import streamlit as st
import pandas as pd
import numpy as np
import pickle


from input_features import user_input_features
from prediction_images import display_prediction_images

data_path = 'cleaned.csv'
data = pd.read_csv(data_path)


# Load the preprocessor and model
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)
    
with open('best_logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)






st.sidebar.write("### Enter the features:")

    # Use the imported function to get user input
input_df = user_input_features()






# Assuming the prediction process is done within this block
if st.sidebar.button('Predict'): 
    processed_input = preprocessor.transform(input_df)
    prediction = model.predict(processed_input)
    st.write(f'# Predicted species: {prediction[0]}')
    # Call the function with the prediction result
    display_prediction_images(prediction[0])