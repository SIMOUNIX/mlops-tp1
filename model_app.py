import joblib
import streamlit as st

# load the model

model = joblib.load('regression.joblib')

st.sidebar.title('House Price Prediction')
st.sidebar.subheader('Enter the details of the house to predict the price')
size = st.sidebar.number_input('Enter the size of the house in m2', min_value=0, max_value=1000, value=0, step=1, key='size')
bedrooms = st.sidebar.number_input('Enter the number of bedrooms', min_value=0, max_value=10, value=0, step=1, key='bedrooms')
garden = st.sidebar.number_input('Has the house a garden ?', min_value=0, max_value=1, value=0, step=1, key='garden')

# if button is clicked, make the prediction and display it
if st.sidebar.button('Predict'):
    prediction = model.predict([[size, bedrooms, garden]])
    print(prediction)
    st.write(f'The predicted price of the house is {prediction[0]}')