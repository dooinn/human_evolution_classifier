import streamlit as st
import pandas as pd


def user_input_features():
    current_country = st.selectbox('Current Country', ['Kenya', 'Republic of Chad', 'Germany', 'Ethiopia', 'Indonesia', 'South Africa', 'Georgia', 'Spain'])
    habitat = st.selectbox('Habitat', ['forest-gallery', 'mixed', 'cold forest', 'forest', 'savannah', 'jungle', 'all', 'peninsular', 'forest-savanna']) 
    
    cranial_capacity = st.number_input('Cranial Capacity (cc)', min_value=50.0, max_value=2000.0, value=400.0)

    jaw_shape = st.selectbox('Jaw Shape', ['U shape', 'conical', 'modern', 'V shape', 'very modern'])

    prognathism = st.selectbox('Prognathism', ['very high','high','medium-high','medium','reduced','very reduced','absent'])

    height = st.number_input('Height (cm)', min_value=50.0, max_value=250.0, value=160.0)
    skeleton = st.selectbox('Skeleton', ['light','refined','robust'])

    hip = st.selectbox('Hip', ['wide', 'slim', 'very modern', 'modern']) 
    foots = st.selectbox('Foots', ['climbing', 'walk'])
    biped = st.selectbox('Biped', ['low probability','high probability','yes','modern'])  
    arms = st.selectbox('Arms', ['climbing','manipulate','manipulate with precision'])
    
    sexual_dimorphism = st.selectbox('Sexual Dimorphism', ['reduced','medium-high','high']) 
    

    diet = st.selectbox('Diet', ['dry fruits', 'carnivorous', 'hard fruits', 'omnivore', 'soft fruits'])

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