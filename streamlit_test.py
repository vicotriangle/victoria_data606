#!pip install -r requirements.txt
import streamlit as st
import pandas as pd
import numpy as np
#import lightgbm as ltb
import pickle


def predict(room_type, host_is_superhost, accommodates, bedrooms, new_bathroom, review_scores_rating):
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

    if Neighbourhood_group_cleansed == 'Manhattan':
        bor_coeff = 36.85
    elif Neighbourhood_group_cleansed == 'Brooklyn':
        bor_coeff = 0
    elif Neighbourhood_group_cleansed == 'Queens':
        bor_coeff = -15.03
    elif Neighbourhood_group_cleansed == 'Bronx':
        bor_coeff = -25.01

    if 'TV' in amenities:
        TV_CE = 14.96
    elif 'TV' not in amenities:
        TV_CE = 0

    if 'Kitchen' in amenities:
        Kit_CE = -28.42
    elif 'Kitchen' not in amenities:
        Kit_CE = 0

    if 'Washer' in amenities:
        Wash_CE = 13.66
    elif 'Washer' not in amenities:
        Wash_CE = 0


    prediction = room_type*27.86+host_is_superhost*11.85+accommodates*11.10+bedrooms*17.21+new_bathroom*7.87+review_scores_rating*13.07+bor_coeff+TV_CE+Kit_CE+Wash_CE
    return prediction
    
st.title('AirBnB Daily Price Analyzer')
st.markdown('Determine if you are charging the right amount for your AirBnB.')
st.header('Enter the characteristics of your AirBnB:')

room_type = st.selectbox("Room Type: ", ['Entire home/apt', 'Private room','Shared room','Hotel room'])
host_is_superhost = st.radio("Are you a Superhost?: ", ('No', 'Yes'))
accommodates = st.number_input("Enter max of occupancy: ", step=1,value=1, min_value=1, max_value=10)
bedrooms = st.number_input("Enter number of bedrooms: ", step=1,value=0, min_value=0, max_value=6)
new_bathroom = st.number_input("Enter number of bathrooms: ", step=1,value=1, min_value=1, max_value=4)
review_scores_rating = st.number_input("Enter current AirBnB rating: ")
amenities = st.multiselect("Amenities: ", ['TV', 'Kitchen', 'Washer'])
Neighbourhood_group_cleansed = st.selectbox("Select Borough: ", ['Manhattan','Queens', 'Brooklyn' ,'Bronx'])


if st.button('Predict Price'):
    price = predict(room_type, host_is_superhost, accommodates, bedrooms, new_bathroom, review_scores_rating)
    st.success(f'The market price of the AirBnB is ${price:.2f} USD')

