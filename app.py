import streamlit as st
import pandas as pd
import numpy as np
import pickle

from input_features import user_input_features

data_path = 'cleaned.csv'
data = pd.read_csv(data_path)


# Load the preprocessor and model
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)
    
with open('best_logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)


def main():
    st.title("# Genus Species Prediction App")
    st.write("### Enter the features:")

    # Use the imported function to get user input
    input_df = user_input_features()

    # Add a button to perform prediction
    if st.button('Predict'):  # This creates a button in the app that, when clicked, triggers the code below
        processed_input = preprocessor.transform(input_df)
        prediction = model.predict(processed_input)
        
        # Display the prediction result
        st.write(f'## Prediction: {prediction[0]}')

if __name__ == "__main__":
    main()

