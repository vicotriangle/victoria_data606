# Proposal
June 4, 2023

## Purpose
Real Estate and travel are passions of mine. I frequently use accommodation applications such as AirBnb, VRBO, Zillow, Realtor.com, etc. to explore, visit, and book properties all around the world. One thing that is an intriguing thought is that there must be a recipe that hosts of successful accommodations follow, or a pattern of attributes about properties, amenities, and overall experience that make those properties good candidates for renting out for short stays in a profitable way. This project attempts to solve for this recipe.
The data being used for this project are details on AirBnb listings in New York City. This project is intended to determine what attributes of an AirBnb listing make them the most successful. Success will be measured by bnb rating, bnb price, and the future availability percentage. Attributes include property description, reviews, NYC neighborhood, property type, room type, host rating, host response rate, host response time, host acceptance rate, number of beds, number of bedrooms, number of baths, and amenities.

## Goals
Overall, if I were to invest in an Airbnb in New York, what parameters should I look for in a real estate listing, how should I write a descriptions to maximize my chances of a successful and profitable Airbnb?
The process of understanding successful Airbnbs will include the following:
1. Use machine learning to predict price based on several parameters from the listings. The plan is to use decision trees, linear regression, and k-means to understand which parameters are most important to a successful bnb.

## Data Source
This data comes from Kaggle at the link: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv.
There are 2 files of raw data from Kaggle. The first is 88KB and includes 37k Airbnb listings from New York City from September 2022. It contains 74 fields of information including important fields such as text fields (name, description, list of amenities, about the host, bathroom text), images (main picture of listing, host thumbnail), categorical (city, neighborhood, type of property, whether the listing is instant bookable), and numerical (listing ID, price, host response rate, latitude, longitude, number of beds, number of bedrooms, number of reviews, average review). The second file is 302MB and includes 986k reviews for each of the listings in the first file. It includes listing ID, review text, the person who reviewed the listing, and the date of review. The descriptions for each of the columns can be found here:https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596.

## Preliminary EDA Results
The preliminary analysis of the data confirmed that this data is interesting and usable. The first check done was to look at the frequency of column nulls. In general, the listings data was highly populated which is a good sign. The reviews dataset was missing only about 200 out of almost 1 million rows. These 200 were removed to be diligent about clean data. Datatypes were changed as appropriate for the columns that were imported in an unusable format. For example, price was a string that included a "$" that needed to be fixed. The dollar sign was removed, and the column was converted to a float which will make it usable later. There was one column "bathrooms" that contained no data, but it was discovered that column "bathroom text" contained the number of bathrooms and the bathroom type of "private" or "shared". This column was used to extract the number of bathrooms for later usability.
Standard statistics were taken for every numerical column. Some of the fields including accommodates, host listings count, and beds had dramatic outliers. When travelers rated their stays, the attribute with the largest standard deviation was cleanliness. Also, by looking at correlation data, it was found that travelers' rating of value of the experience was the highest predictor of overall rating. No other correlations were terribly helpful in that they accurately trended with price or ratings.
A heat map was made on a scatter plot of ratings versus prices to understand their distribution and density. It was found that listings with a price of just under $100 and a rating of 5.0 were the most common. the data was cleaned up to include only the middle 80% of prices and the top 75% of ratings.
Histograms were then created to understand the resulting distribution after data was cleaned. This was used to confirm that the data is relatively clean and ready to be used.


## Challenges:
1. Importing the data directly from Google Drive is not working. A workaround was created so that the script will download the file properly from Google Drive to the user's local drive before it is loaded into the Python kernel. This may need to be fixed.
2. Translating the reviews that were not in English did not work. Needs more research into the impact of not translating or another solution.
