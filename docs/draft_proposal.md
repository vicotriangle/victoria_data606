# Proposal
June 4, 2023

## Purpose
Real Estate and travel are passions of mine. I frequently use accommodation services such as AirBnb, VRBO, Zillow, Realtor.com, etc. to explore, visit, and book properties all around the world. One thing that is an intriguing thought is that there must be a recipe that hosts of successful accommodations follow, or a pattern of attributes about properties, amenities, and overall experience that make those properties good candidates for renting out for short stays in a profitable way. This project attempts to understand what features of an Airbnb contributes to its daily price.
The data being used for this project are details on AirBnb listings in New York City. Success will be measured using RMSE on the machine learning models. Attributes include NYC neighborhood, property type, room type, ratings, number of beds, number of bedrooms, number of baths, and amenities.

## Goals
Overall, if I were to invest in an Airbnb in New York, what parameters should I look for in a real estate listing, how should I write a descriptions to maximize my chances of a successful and profitable Airbnb?
The process of understanding successful Airbnbs will include the following:
1. Use machine learning to predict price based on several parameters from the listings. The plan is to use decision trees, linear regression, and k-means to understand which parameters are most important to a successful bnb.

## Data Source
This data comes from Kaggle at the link: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv.
There are 2 files of raw data from Kaggle. The first is 88KB and includes 37k Airbnb listings from New York City from September 2022. It contains 74 fields of information including important fields such as text fields (name, description, list of amenities, about the host, bathroom text), images (main picture of listing, host thumbnail), categorical (city, neighborhood, type of property, whether the listing is instant bookable), and numerical (listing ID, price, host response rate, latitude, longitude, number of beds, number of bedrooms, number of reviews, average review). The second file is 302MB and includes 986k reviews for each of the listings in the first file. It includes listing ID, review text, the person who reviewed the listing, and the date of review. The descriptions for each of the columns can be found here:https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596.
