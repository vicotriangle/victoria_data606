import streamlit as st
import pandas as pd
import numpy as np
import pickle

def predict(room_type, host_is_superhost): #, accommodates, bedrooms, new_bathroom, review_scores_rating):
    #Predicting the price of the AirBnb
    if room_type == 'Hotel room':
        room_type = 3
    elif room_type == 'Entire home/apt':
        room_type = 4
    elif room_type == 'Private room':
        room_type = 2
    elif room_type == 'Shared room':
        room_type = 1

    if host_is_superhost == 'No':
        host_is_superhost = 0
    elif host_is_superhost == 'Yes':
        host_is_superhost = 1


    prediction = room_type*37.65+host_is_superhost*11.85#+bedrooms*17.21+review_scores_rating*13.07+accommodates*11.10+new_bathroom*7.87
    return prediction
    


st.title('AirBnB Price Predictoraaa')
st.markdown('Determine if you are charging the right amount for your AirBnB.')
st.header('Enter the characteristics of your AirBnB:')

room_type = st.selectbox("Room Type: ", ['Entire home/apt', 'Private room','Shared room','Hotel room'])
host_is_superhost = st.radio("Are you a Superhost?: ", ('No', 'Yes'))
accommodates = st.number_input("Enter max of occupancy: ", step=1)
bedrooms = st.number_input("Enter number of bedrooms: ", step=1)
new_bathroom = st.number_input("Enter number of bathrooms: ", step=1)
review_scores_rating = st.number_input("Enter current AirBnB rating: ")
amenities = st.multiselect("Amenities: ", ['TV', 'Kitchen', 'Washer'])
Neighbourhood_group_cleansed = bedrooms = st.selectbox("Select Borough: ", ['Manhattan','Queens', 'Brooklyn' ,'Bronx'])


if st.button('Predict Price'):
    price = predict(room_type, host_is_superhost)
    st.success(f'The predicted price of the AirBnB is ${price:.2f} USD')
