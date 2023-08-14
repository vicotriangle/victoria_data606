Victoria Borsetti

August 1, 2023

### Description:
This analysis will use Airbnb data from New York City to determine what aspects of a bnb listing contribute most to their price.

Overall, if I owned an Airbnb in NYC, what are the features that would help me set an accurate cost and how much?
The process of understanding Airbnb prices will include the following:
1. Clean the data.
2. Use machine learning to predict price based on several parameters from the listings. The plan is to use linear regression, polynomial regression, and LazyPredict (to find the best model) to understand which parameters are most important to a bnb's price.
3. Add in data for locations of subway stations to see if "convenience" contributes to a better model.
4. Re-analyze models for best fit.

### Source:
1. Airbnb data comes from Kaggle at the link: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv  
Column descriptions can be found at the link: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596

The file from Kaggle is 88MB and includes 37k Airbnb listings from New York City downloaded in June of 2022. It contains 74 fields of information including important fields such as text fields (name, description, list of amenities, about the host, bathroom text), images (main picture of lisitng, host thumbnail), categorical (city, neighborhood, type of property, whether the listing is instant bookable), and numerical (listing ID, price, host response rate, latitude, longitude, number of beds, number of bedrooms, number of reviews, average review).

2. Additional Sources used include NYC subway station location data found on New York City MTA site. This data can be found here:https://data.ny.gov/widgets/i9wp-a4ja

The file from New York City Stations Database is 457kB and includes 1.8k records and 34 fields. The only fields used in this analysis are longitude and latitude of station entrances.
