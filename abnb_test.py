
import streamlit as st
import pandas as pd
import numpy as np



st.title('AirBnB Price Predictor')
st.markdown('Determine if you are charging the right amount for your AirBnB.')
st.header('Enter the characteristics of your AirBnB:')


#model = ltb.LGBMRegressor()
#model.load_model('lgbm_model.json')


room_type = st.selectbox("Room Type: ",
                     ['Hotel room', 'Entire home/apt' ,'Private room','Shared room'])
host_is_superhost = st.radio("Are you a Superhost?: ", ('No', 'Yes'))
accommodates = st.number_input("Enter max of occupancy: ", step=1)
bedrooms = st.number_input("Enter number of bedrooms: ", step=1)
new_bathroom = st.number_input("Enter number of bathrooms: ", step=1)
review_scores_rating = st.number_input("Enter current AirBnB rating: ")
amenities = st.multiselect("Amenities: ",
                         ['TV', 'Kitchen', 'Washer'])
Neighbourhood_group_cleansed = bedrooms = st.selectbox("Select Borough: ",
                     ['Manhattan','Queens', 'Brooklyn' ,'Bronx'])
st.button("Predict Price")