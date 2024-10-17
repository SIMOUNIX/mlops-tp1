import streamlit as st
import requests
import json

st.sidebar.title('House Price Prediction')
st.sidebar.subheader('Enter the details of the house to predict the price')
size = st.sidebar.number_input('Enter the size of the house in m2', min_value=0, max_value=1000, value=0, step=1, key='size')
bedrooms = st.sidebar.number_input('Enter the number of bedrooms', min_value=0, max_value=10, value=0, step=1, key='bedrooms')
garden = st.sidebar.number_input('Has the house a garden ?', min_value=0, max_value=1, value=0, step=1, key='garden')

features = {"size": size, "nb_rooms": bedrooms, "garden": garden}

# if button is clicked, make the prediction and display it
if st.sidebar.button('Predict'):
    res = requests.post(url="http://localhost:8000/predict", data=json.dumps(features))
    st.write(f'The predicted price of the house is {res.json()["prediction"]}')