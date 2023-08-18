Victoria

August 1, 2023

https://github.com/vicotriangle/victoria_data606/blob/main/docs/capstone.pptx

### Overview
Real Estate and travel are passions of mine. I frequently use accommodation services such as AirBnb, VRBO, Zillow, Realtor.com, etc. to explore, visit, and book properties all around the world. One thing that is an intriguing thought is that there must be a recipe that hosts of successful accommodations follow, or a pattern of attributes about properties, amenities, and overall experience that make those properties good candidates for renting out for short stays in a profitable way. This project attempts to understand what features of an Airbnb contributes to its daily price. The data being used for this project are details on AirBnb listings in New York City. Success will be measured using RMSE on the machine learning models. Attributes include NYC neighborhood, property type, room type, ratings, number of beds, number of bedrooms, number of baths, and amenities.

### Method:
This analysis will use Airbnb data from New York City to determine what aspects of a bnb listing contribute most to their price.

Overall, if I were an Airbnb investor in NYC, what are the features that would help me set an accurate daily cost? How can I use this information to develop a strategy for my Airbnb investment that aligns with my goals for competitive price versus booking percentage?
To meet these goals, the following steps will be performed:
1. Clean the data.
2. Perform NLP on the string fields were appropriate.
3. Use machine learning to predict price based on several parameters from the listings. The plan is to use linear regression (for feature selection), polynomial regression, and LazyPredict (to find the best additional model) to understand which parameters are most important to a bnb's price and to accurately predict price. Use RMSE for measuring success.
5. Add in data for locations of subway stations to see if "convenience" contributes to a better fit model.
6. Re-analyze models for best fit. Use RMSE to re-measure success.
7. Create a web app with a user-friendly interface that could be used by an investor to assist them in understanding the price elements of their Airbnb.

### Source:
1. Airbnb data comes from Kaggle at the link: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv  
Column descriptions can be found at the link: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596

The file from Kaggle is 88MB and includes 37k Airbnb listings from New York City downloaded in June of 2022. It contains 74 fields of information including important fields such as text fields (name, description, list of amenities, about the host, bathroom text), images (main picture of lisitng, host thumbnail), categorical (city, neighborhood, type of property, whether the listing is instant bookable), and numerical (listing ID, price, host response rate, latitude, longitude, number of beds, number of bedrooms, number of reviews, average review).

2. Additional Sources used include NYC subway station location data found on New York City MTA site. This data can be found here:https://data.ny.gov/widgets/i9wp-a4ja

The file from New York City Stations Database is 457kB and includes 1.8k records and 34 fields. The only fields used in this analysis are longitude and latitude of station entrances.
