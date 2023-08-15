# Using Machine Learning to Analyze Airbnb Prices

**Author:** Victoria Borsetti \
**Course:** Capstone in Data Science \
**Term:** Summer 2023

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/acff7126-38cb-4d52-b7af-68f4a96e62e7)

## Overview

### Background
Real Estate and travel are passions of mine. I frequently use accommodation services such as AirBnb, VRBO, Zillow, Realtor.com, etc. to explore, visit, and book properties all around the world. Currently, for Airbnb investors, it is difficult to perceive market fluctuations and monitor the supply and demand of accommodation options to ensure a competitive, yet profitable daily cost. There is no direct way to analyze comparable homes, understand what attributes of the Airbnb demand a higher rate, or identify issues in the listing that are affecting bookings. The impact of this is profit loss on homes priced too low, low booking rates on homes priced too high, and poor investment management due to the "black-box" nature of Airbnb cost setting.

### Purpose
An intriguing thought is that there is likely a recipe that can help determine an appropriate daily cost for an Airbnb based on typical property features, location, amenities, and overall experience ratings. This project attempts the following:
1. Use machine learning to understand what attributes of an Airbnb contribute most to its price.
2. Create a webapp where an investor could input key information of their listing, and using a machine learning model, could calculate the market cost of their Airbnb.

### Data Sources
The data being used for this project are details of Airbnb listings in New York City that are scraped from the site by a third-party source. Success will be measured using RMSE on the machine learning models. Attributes include NYC neighborhood, property type, room type, ratings, number of beds, number of bedrooms, number of baths, and amenities.
This analysis will use Airbnb data from New York City to determine what aspects of a bnb listing contribute most to their price.

1. Airbnb data comes from Kaggle at the link: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv  
Column descriptions can be found at the link: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596

The file from Kaggle is 88MB and includes 37k Airbnb listings from New York City downloaded in June of 2022. It contains 74 fields of information including important fields such as text fields (name, description, list of amenities, about the host, bathroom text), images (main picture of lisitng, host thumbnail), categorical (city, neighborhood, type of property, whether the listing is instant bookable), and numerical (listing ID, price, host response rate, latitude, longitude, number of beds, number of bedrooms, number of reviews, average review).

2. Additional Sources used include NYC subway station location data found on New York City MTA site. This data can be found here:https://data.ny.gov/widgets/i9wp-a4ja

The file from New York City Stations Database is 457kB and includes 1.8k records and 34 fields. The only fields used in this analysis are longitude and latitude of station entrances.





## Preliminary EDA Results
The preliminary analysis of the data confirmed that this data is interesting and usable. The first check done was to look at the frequency of column nulls. In general, the listings data was highly populated which is a good sign. The reviews dataset was missing only about 200 out of almost 1 million rows. These 200 were removed to be diligent about clean data. Datatypes were changed as appropriate for the columns that were imported in an unusable format. For example, price was a string that included a "$" that needed to be fixed. The dollar sign was removed, and the column was converted to a float which will make it usable later. There was one column "bathrooms" that contained no data, but it was discovered that column "bathroom text" contained the number of bathrooms and the bathroom type of "private" or "shared". This column was used to extract the number of bathrooms for later usability.
Standard statistics were taken for every numerical column. Some of the fields including accommodates, host listings count, and beds had dramatic outliers. When travelers rated their stays, the attribute with the largest standard deviation was cleanliness. Also, by looking at correlation data, it was found that travelers' rating of value of the experience was the highest predictor of overall rating. No other correlations were terribly helpful in that they accurately trended with price or ratings.
A heat map was made on a scatter plot of ratings versus prices to understand their distribution and density. It was found that listings with a price of just under $100 and a rating of 5.0 were the most common. the data was cleaned up to include only the middle 80% of prices and the top 75% of ratings.
Histograms were then created to understand the resulting distribution after data was cleaned. This was used to confirm that the data is relatively clean and ready to be used.


## Challenges:
1. Importing the data directly from Google Drive is not working. A workaround was created so that the script will download the file properly from Google Drive to the user's local drive before it is loaded into the Python kernel. This may need to be fixed.
2. Translating the reviews that were not in English did not work. Needs more research into the impact of not translating or another solution.
