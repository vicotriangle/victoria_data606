# Using Machine Learning to Analyze Airbnb Prices

**Author:** Victoria Borsetti \
**Course:** Capstone in Data Science \
**Term:** Summer 2023

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/acff7126-38cb-4d52-b7af-68f4a96e62e7)


## Table of Contents
[**Overview**](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#overview)
  - [Background](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#background)
  - [Purpose](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#purpose)
  - [Data Sources](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#data-sources)
  - [Approach](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#approach)

[**Execution**](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#execution)
  - [Preliminary Data Exploration](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#preliminary-data-exploration)
  - [Model Development](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#model-development)
    - [Data Cleansing](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#data-cleansing)
    - [Encoding Categorical Columns](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#encoding-categorical-columns)
    - [Natural Language Processing](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#natural-language-processing)
    - [Normalization & Feature Selection](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#normalization--feature-selection)
    - [Adding in Supplemental Subway Station Data](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#adding-in-supplemental-subway-station-data)
    - [Lazy Predict](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#lazy-predict)
    - [Machine Learning](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#machine-learning)
  - [Deployment](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#deployment)

[**Conclusion**](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#conclusion)
  - [Interpretation of Results](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#interpretation-of-results)
    - [Analysis of Features](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#analysis-of-features)
    - [Analysis of Machine Learning Models](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#analysis-of-machine-learning-models)
    - [Analysis of Deployment Application](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#analysis-of-deployment-application)
  - [Learnings](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#learnings)
  - [Future Research](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#future-research)



## Overview

### Background
Real Estate and travel are passions of mine. I frequently use accommodation services such as Airbnb, VRBO, Zillow, Realtor.com, etc. to explore, visit, and book properties all around the world. Currently, for Airbnb investors, it is difficult to perceive market fluctuations and monitor the supply and demand of accommodation options to ensure a competitive, yet profitable daily cost. There is no direct way to analyze comparable homes, understand what attributes of the Airbnb demand a higher rate, or identify issues in the listing that are affecting bookings. The impact of this is profit loss on homes priced too low, low booking rates on homes priced too high, and poor investment management due to the "black-box" nature of Airbnb cost setting.

### Purpose
Perhaps there is a recipe that can determine an appropriate daily cost for an Airbnb based on typical property features, location, amenities, and overall experience ratings. This project attempts the following:
1. Use machine learning to understand what attributes of an Airbnb contribute most to its price.
2. Create a webapp where an investor could input key information of their listing, and using a machine learning model, could calculate the market cost of their Airbnb.

### Data Sources
#### Primary Data
The data being used for this project are details of Airbnb listings in New York City that were scraped from the site by a third-party.

  - Airbnb data comes from [Kaggle](https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv)
  - [Metadata](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596) is available for column descriptions and is displayed below.

The file from Kaggle is 88MB and includes 37k Airbnb listings from New York City downloaded in June of 2022. It contains 74 fields of information. The full list and description of the fields are as follows:

**id** (int) = primary key of Airbnb listings \
**listing_url** (string) = url link for the Airbnb listing \
**scrape_id** (int) = identifier for scrape event \
**last_scraped** (datetime) = the date and time the listing was scraped \
**source** (string) = what kind of scrape the listing was found \
**name** (string) = what the host named the Airbnb \
**description** (string) = host's description of the listing \
**neighborhood_overview** (string) = host's description of the neighborhood \
**picture_url** (string) = url of the primary image of the Airbnb \
**host_id** (int) = Airbnb's unique identifier for hosts \
**host_url** (string) = url of host profile \
**host_name** (string) = name of host \
**host_since** (datetime) = date host has been active since \
**host_location** (string) = self-reported location of the host \
**host_about** (string) = host's description of themselves \
**host_response_time** (string) = categorical description of how long it typically takes host to respond to a message \
**host_response_rate** (string) = percentage of time a host responds to a message \
**host_acceptance_rate** (string) = percentage of time host accepts a request to book \
**host_is_superhost** (boolean) = boolean t/f for whether host is a superhost \
**host_thumbnail_url** (string) = url for host profile picture - small size \
**host_picture_url** (string) = url for host profile picture - medium size \
**host_neighbourhood** (string) = self-reported neighborhood location of the host \
**host_listings_count** (int) = how many listings host has in total \
**host_total_listings_count** (int) = how many listings host has in total \
**host_verifications** (string) = list of methods host used to verify their identity \
**host_has_profile_pic** (boolean) = boolean t/f for whether host has a profile picture \
**host_identity_verified** (boolean) = boolean t/f for whether host has verified their identitiy using any method \
**neighbourhood** (string) = neighborhood listing is located in \
**neighbourhood_cleansed** (string) = neighborhood in which listing is located \
**neighbourhood_group_cleansed** (string) = neighborhood in which listing is located - cleaned for consistency \
**latitude** (float) = latitude of Airbnb listing location \
**longitude** (float) = longitude of Airbnb listing location \
**property_type** (string) = categorical description of type of property (house, castle, loft, boat, campsite, etc.) \
**room_type** (string) = categorical description of type of room (entire home, private room, shared room, hotel room) \
**accommodates** (int) = number of people the listing accommodates \
**bathrooms** (int) = number of bathrooms \
**bathrooms_text** (string) = number and type of bathroom \
**bedrooms** (int) = number of bedrooms \
**beds** (int) = number of beds \
**amenities** (string) = list of all amenities the listing offers (wifi, kitchen, hot tub, washer, dryer, air conditioning, etc.) \
**price** (string) = daily cost of the property \
**minimum_nights** (int) = minimum nights host requires guest to stay \
**maximum_nights** (int) = maximum nights host allows guest to stay \
**minimum_minimum_nights** (int) = smallest minimum night stay required looking 365 days into the future \
**maximum_minimum_nights** (int) = largest minimum night stay required looking 365 days into the future \
**minimum_maximum_nights** (int) = smallest maximum night stay allowed looking 365 days into the future \
**maximum_maximum_nights** (int) = largest maximum night stay allowed looking 365 days into the future \
**minimum_nights_avg_ntm** (int) = average minimum night stay required looking 365 days into the future \
**maximum_nights_avg_ntm** (int) = average maximum night stay allowed looking 365 days into the future \
**calendar_updated** (datetime) = the last date the host updated the calendar \
**has_availability** (boolean) = boolean t/f for whether the listing has availability in the future \
**availability_30** (int) = number of nights of availability in the next 30 days \
**availability_60** (int) = number of nights of availability in the next 60 days \
**availability_90** (int) = number of nights of availability in the next 90 days \
**availability_365** (int) = number of nights of availability in the next 365 days \
**calendar_last_scraped** (datetime) = last date the listing's calendar was scraped \
**number_of_reviews** (int) = number of total reviews the listing has ever \
**number_of_reviews_ltm** (int) = number of reviews the listing had in the last 12 months \
**number_of_reviews_l30d** (int) = number of reviews the listing had in the last 30 days \
**first_review** (datetime) = date of the listing's first review \
**last_review** (datetime) = date of the listing's first review \
**review_scores_rating** (float) = average overall guest review rating for the listing \
**review_scores_accuracy** (float) = average guest review rating for how accurate the listing was compared to guest's experience \
**review_scores_cleanliness** (float) = average guest review rating for how clean the property was \
**review_scores_checkin** (float) = average guest review rating for simplicity of checking in to the property upon arrival \
**review_scores_communication** (float) = average guest review rating for quality of communication from the host \
**review_scores_location** (float) = average guest review rating for location of the property \
**review_scores_value** (float) = average guest review rating for the value of the stay \
**license** (string) = The license/permit/registration number of the listing \
**instant_bookable** (boolean) = boolean t/f for whether the guest can automatically book the listing without host acceptance \
**calculated_host_listings_count** (int) = total number of listings the host has \
**calculated_host_listings_count_entire_homes** (int) = total number of listings the host has that are entire homes \
**calculated_host_listings_count_private_rooms** (int) = total number of listings the host has that are private rooms \
**calculated_host_listings_count_shared_rooms** (int) = total number of listings the host has that are shared rooms \
**reviews_per_month** (int) = average number of reviews the listing gets per month \


#### Supplemental Data
The hypothesis behind additional data is that an attribute that quantifies convenience of location of an Airbnb may affect its daily price. Subway station location data is available through the NYC Metropolitan Transportation Authority. Calculating distance to the nearest station may contribute to a more accurate model.

  - [Subway Station Locations](https://data.ny.gov/widgets/i9wp-a4ja) are made available by the state of NY

The file from New York City Stations Database is 457kB and includes 1.8k records and 34 fields. The only fields used in this project are longitude and latitude of station entrances so they can be compared to longitudes and latitudes of each Airbnb.

### Approach
All code, documents, and presentations will be published to [Github](https://github.com/vicotriangle/victoria_data606/blob/main/). Python will be used for data exploration and model development through Google Colab (.ipynb). Streamlit will be used to create the user interface for the webapp, VSCode for editing, and GitHub as the deployment source for StreamLit.
The procedure used for this project includes the following:
1.	Preliminary Data Exploration
2.	Model Development
    -	Data Cleansing
    -	Encoding Categorical Columns
    -	Natural Language Processing
    -	Normalization & Feature Selection
    -	Add in Supplemental Subway Station Data
    -	Lazy Predict
    -	Machine Learning
3.	Deployment

## Execution

### Preliminary Data Exploration
The preliminary analysis of the data confirmed that this dataset is informative and usable. This section outlines the checks used to come to this conclusion.

#### Airbnb Map
To get a visual of the data, longitude and latitude is plotted for each Airbnb. In the image below, Staten Island data is sparse. To the left of Manhattan, there appears to be Airbnbs included that are actually in New Jersey. These anomalies will have to be handled before this data can be used in a machine learning model.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/57ae0147-f572-41c1-8d81-41230d699486)


#### Statistics
The shape of the data is 37,410 rows by 74 columns. Many of the fields can be eliminated based on their description as they will not improve the price prediction model. These include the url fields, description fields, host information, and scrape information. Frequency of column nulls is checked using the visual below to ensure enough data is present for proper analysis. In general, the listings data has a high rate of populated fields. Important fields like price, longitude, latitude, number of reviews, property type, room type, accommodates and amenities all have data for every listing. These are key fields that will be crucial for the goal of predicting price. Bathrooms, calendar updated, and license are largely unused and may be deleted. For the fields that contain an acceptable amount of blanks such as review scores, beds, bedrooms, and bathroom text, a strategy for handling these will have to be decided on during data cleansing. These are not in quantities that will materially impact results.

Columns with significant null rates are shown below.
![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/b77b9d79-b59b-4c75-a84e-956fa2c74ffb)

Datatypes need to be changed as appropriate for the columns that are in an unusable format. For example, price is a string that includes a "$" that needs to be removed and converted to float. There is one column "bathrooms" that contains no data, but it is discovered that column "bathroom text" contains the number of bathrooms and the bathroom type of "private" or "shared" which can be extracted, split and used in place of "bathrooms". Standard statistics are taken for every numerical column. Some of the fields including accommodates, host listings count, and beds have dramatic outliers, although this will not materially affect the usability of the dataset. There is a sufficient amount of data to accommodate substantial data cleansing even if all outliers are removed. 

To supplement the outlier observation for price that was made initially, a boxplot is used to visualize the distribution of values. It will be important to remove a significant amount of data that sits outside of a few standard deviations from the mean. If not, the model will be less accurate.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/8c896663-2d40-461b-a82f-0f30aec6de61)


Charts such as histograms, tables, and correlation scatterplots did not expose any further insights beyond the discovery that this data is dramatically right-skewed. Correlation plots with all columns versus price did not reveal strong trends, but did have loose relationships for key fields mentioned above that will be exploited later.

A heatmap is made on a scatter plot of the key field, overall ratings versus prices to understand their distribution and density. Listings with a price of just under $100 and a rating near 5.0 are the most common.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/2e1524c4-384c-4824-b7d6-d31fa0287916)


Likewise, a density heatmap of the key field representing the number of people a listing accommodates versus price is created to see if there is an obvious trend. The most common accommodation is for that of 2 to 3 guests. There is a slight correlation to price, but since data is so dense at very low cost, the outliers of price and accommodates make it difficult to observe.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/f6f6e7e2-af31-44f3-9e7c-3c39828e1b9c)

To see the distribution of room types, another key field, a bar chart is created. The listings in this dataset are largely entire homes and private rooms.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/deed3215-cad0-487c-99f8-87f585adc872)


For the purposes of this project, this data is deemed usable based on rate of populated key fields, volume of data points, minimal data quality issues, and presence of fields expected to impact price most highly.


### Model Development

#### Data Cleansing
Per the observations in the preliminary exploration, there is significant data cleansing and analysis required to understand what data is most helpful to keep. For each of these steps, linear regression was used to supervise what changes improved/hurt the model's accuracy using RMSE as the measure. The following steps were followed and discoveries made.
1. 43 columns were removed as they will not correlate to price. 31 fields remain that have potential to contribute to price including:
   - id
   - host_is_superhost
   - neighboorhood_cleansed
   - neighborhood_group_cleansed (borough)
   - latitude
   - longitude
   - property_type
   - room_type
   - accommodates
   - bathrooms_text
   - bedrooms
   - beds
   - amenities
   - price
   - minimum_nights
   - availability_30
   - availability_60
   - availability_90
   - availability_365
   - number_of_reviews
   - number_of_reviews_ltm
   - number_of_reviews_l30d
   - review_scores_rating
   - review_scores_accuracy
   - review_scores_cleanliness
   - review_scores_checkin
   - review_scores_communication
   - review_scores_location
   - review_scores_value
   - calculated_host_listings_count
   - reviews_per_month
2. Price field was reformatted to remove the dollar sign and converted to float.
3. Airbnbs in the dataset that had $0 for price were removed as these will throw off the model. This scenario happens when a host makes the listing unavailable or the listing is brand new.
4. Price outliers were handled using interquartile method. Prices outside of 1.5x the interquartile range (0.25-0.75) were excluded. This will make the model more accurate as the data will have less skew.
5. Airbnbs in the dataset that had an overall review rating of 0 were removed. Analysis of these rows revealed that these are auto-generated reviews from Airbnb when a host cancels a guest's reservation. This was found to skew the machine learning model's accuracy while keeping all else equal.
6. Airbnbs in the dataset that had less than 3 total reviews were removed as their inclusion affected accuracy of the model. Likely 2 or less reviews are not enough to get an accurate measure of the quality of a bnb.
7. Bathrooms_text was split into two fields to make them usable.
   - **new_bathroom** (float) = count of bathrooms
   - **new_bathroom_type** (string) = type of bathroom (private or shared)
8. Staten Island datapoints were removed because the data was sparse, and Staten Island does not have standard subway stations data available.
9. New Jersey datapoints were removed using brute-force method of excluding points outside of several squares. This data is not helpful and subway station data is not available for this area.
10. Nulls were filled using a tailored approach for each column that contained nulls:
    - bedrooms nulls were filled with 0. The rows that were spot checked were largely studio apartments where the host did not fill in the number of bedrooms field.
    - beds nulls were filled with 1. Likely there will be at least one bed offered.
    - all review_scores fields' nulls were filled with the average of that column. This will allow for an even distribution that won't affect the mean.
    - reviews_per_month nulls were filled with its average.
    - new_bathroom_type nulls were filled with "private". Likely, if a host doesn't specify, the bathroom is not shared.
    - host_is_superhost nulls were filled with "f" for false as hosts would want this populated to get higher demand if it were true.

After this cleanup, the dataset contains 20,851 Airbnb listings and 32 information fields. The map below shows the results of datapoint removal.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/8dcc38f0-237c-4e26-9e9a-f607b75eb155)


#### Encoding Categorical columns
In order to use a machine learning model, all columns have to be numerical. There are 6 columns that are categorical and an appropriate conversion to numbers must be selected. The following encoding methods were performed per each column:
1. Room_type was encoded based on desirability of the value because there is a meaningful hierarchy. By doing this, the machine learning algorithm can take into account the ordinality of the field.
   - entire home/apt = 4
   - hotel room = 3
   - private room = 2
   - shared room = 1
2. Bathroom_type was encoded based on desirability of the value because there is a meaningful hierarchy. By doing this, the machine learning algorithm can take into account the ordinality of the field.
   - private = 1
   - shared = 0
3. Host_is_superhost was encoded based on desirability of the value because there is a meaningful hierarchy. By doing this, the machine learning algorithm can take into account the ordinality of the field.
   - True = 1
   - False = 0
4. Borough was one-hot encoded because there is no ordinality of the values, yet there is a low quantity of unique options. This added 4 new fields to the dataset, one for each borough. If the Airbnb is in that borough, the corresponding column will be "1" and "0" if not. This approach returned better results than using label encoding.
5. Neighborhood was label encoded using sklearn to a random number from 0 to the number of unique values present. Because there is no ordinality and a high quantity of unique options, this was the best choice for this field.
6. Property_type was label encoded using sklearn to a random number from 0 to the number of unique values present. Because there is no ordinality and a high quantity of unique options, this was the best choice for this field.

#### Natural Language Processing
The amenities field contains important features offered by each Airbnb in a list structure. There are 3,776 unique amenities contained in this field. The approach used is to perform natural language processing to determine what the most common amenities are and to later analyze which have the biggest impact on price. The following steps were followed:
1. Concatenate all list items into one text element separated by a space.
2. Tokenization - transforms each word into a discrete element.
3. Remove stop words - common words that do not contribute to meaning of the amenity are removed.
4. Create a table that shows the top 10 amenities and their frequencies:

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/78b9a76b-0b4b-465e-8d1d-f0356e604add)

5. Add this information back into the dataset in the form of one-hot encoding each of the ten amenities into columns. If the Airbnb has that amenity in its amenities column, the corresponding column will be "1" and "0" if not.

#### Normalization & Feature Selection
In order to ensure no one feature is given a stronger weight by the machine learning model, all numerical values are converted to a scale from 0-1. This did not impact the accuracy of the models but is good practice. Feature selection was performed on this dataset using a linear regression model to produce measures of feature importance in the form of coefficients. Multi-collinearity was also considered during feature selection to ensure the model was not overfitting the data. Any correlation above 0.70 was eliminated. The following fields were eliminated based on high correlation with another field, or poor/no impact on the model:
1. Review_scores_accuracy - highly correlated with review_scores_rating (0.81) and did not contribute significantly to the model
2. Review_scores_value - highly correlated with review_scores_rating (0.82) and did not contribute significantly to the model
3. Review_scores_checkin - highly correlated with review_scores_rating (0.67) and did not contribute significantly to the model
4. Review_scores_communication - did not contribute significantly to the model
5. Review_scores_cleanliness - highly correlated with review_scores_rating (0.76) and did not contribute significantly to the model
6. Review_scores_rating - highly correlated to review_scores_location (0.50) and did not contribute significantly to the model
7. Number_of_reviews - did not contribute significantly to the model
8. Calculated_host_listings_count - did not contribute significantly to the model
9. Host_is_superhost - did not contribute significantly to the model
10. New_bathroom_type - highly correlated with room_type (0.78)
11. Availability_60 - highly correlated with availability_30 (0.89)
12. Availability_90 - highly correlated with availability_30 (0.81)
13. Availability_365 - highly correlated with availability_30 (0.89)
14. Reviews_per_month - highly correlated with number_of_reviews_ltm (0.80)
15. Beds - highly correlated with accommodates (0.75)
16. Property_type - highly correlated with room_type (0.95)
17. Neighbourhood_cleansed - did not contribute significantly to the model
18. Borough_Brooklyn - highly correlated with borough_Manhattan (0.64) and caused multicollinearity with the other borough columns
19. Minimum_nights - did not contribute significantly to the model
20. Number_of_reviews_l30d - highly correlated with number_of_reviews_ltm (0.63) and did not contribute significantly to the model
21. Cooking - did not contribute significantly to the model
22. Heating - did not contribute significantly to the model
23. Fridge - did not contribute significantly to the model
24. Wifi - did not contribute significantly to the model
25. Essentials - did not contribute significantly to the model
26. Air conditioning - did not contribute significantly to the model
27. Hot tub - did not contribute significantly to the model


The resulting correlation matrix shows no multi-collinearity/strong correlations between fields. This is imperative to ensuring the model is not overfit to the data.
![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/9e079fd4-8b9e-4d70-b9be-2c3ee8c6f2b7)


#### Adding in Supplemental Subway Station Data
A new dataset was added to the notebook to pull in longitude and latitude of subway station entrances. The map of the subway stations confirms that it will span appropriately to all of the Airbnb locations.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/301ee906-ba59-4632-8cec-392b0e0424d0)


Two columns were added to the Airbnb dataset. 'Distance', which will be the distance in feet from the Airbnb to the nearest subway station, and 'accessibility' which will be a flag that is 1 if the closest station is within 2,000ft and 0 if not. 2,000ft was found to be the distance that most improved the model while testing between 500ft and 5,000ft. This is logical, as 2,000 is approximately 3 blocks in NYC terms.
Cdist is a function that takes two sets of longitude and latitude arrays and calculates the distances between every set of points. This can be used to identify the shortest distance for each Airbnb and inserting it into the new 'distance' column. 'Accessibility' is then calculated based on this distance. Between both new columns, 'accessibility' was found to improve the model on its own more. Therefore, 'distance' was removed to avoid overfitting.

##### Final Features

After feature selection and addition of distance, 14 final features prevail. The below table shows the features that most influenced price and their importance. The most important feature is the number of reviews the Airbnb received in the past 12 months, followed by bedrooms, number of people the listing accommodates, rating of the location, room type, etc. 3 features contributed to a lower price including mentioning 'kitchen' in amenities, and having a location in the boroughs of Queens and the Bronx. See [Analysis of Features](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#analysis-of-features) section for more.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/c1811b65-0479-485e-b804-5c3c1c1fb7ca)



#### Lazy Predict
LazyPredict is used to get quick results of many machine learning models and a first approximation of their accuracy. It is found that LGBMRegressor would be the best fit model for this particular data. Documentation for this model is at the link: https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/4784d8d3-1e84-4787-a6d7-5d34c9c6bdda)

#### Machine Learning
The data is ready to be used in machine learning. The three models used are:
1. Linear Regression
2. Polynomial Regression
3. LGBM Regression

##### Linear Regression Results
The linear regression model produced an RMSE of 55.16. This means that on average, the price is off from the target by $55.16 per Airbnb. What is interesting about the resulting chart is that as target price increased by one unit, the predicted price increased at a smaller unit. In other words, the relationship here looks polynomial. Perhaps a polynomial regression model would produce better results.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/1701a8d6-2a13-4485-8783-71d448dba973)



##### Polynomial Regression Results
The polynomial regression model produced an RMSE of 52.60. This means that on average, the price is off from the target by $52.60 per Airbnb. The resulting chart comparing target to predicted price shows a more linear shape indicating a better fit model.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/2b51ad1a-b05f-41ec-9392-08b80e7338e4)


##### LGBM Regression Results
The LGBM regression model produced an RMSE of 49.96. This means that on average, the price is off from the target by $49.96 per Airbnb. The resulting chart comparing target to predicted price shows a tighter figure that indicates a closer trend to target=predicted.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/7ccb10da-672b-4dcd-b694-e23697f5c6b9)


### Deployment
Implementation of a tool that assists Airbnb Investors in understanding the market price of their bnb was built in StreamLit. The model used was a simplified linear regression model that only includes the fields most relevant and most obtainable to an Airbnb host. These include borough, maximum occupancy, room type, number of bedrooms, number of bathrooms, overall rating, and host is superhost. The RMSE of this model is 57.69. This model sacrifices accuracy for usability by about $10 compared to our optimized model with more features.

With these features, the importance of each changes from the original regression model. The most important attribute is whether the property is in Manhattan or not. If so, there is a $37 gain on the daily cost. Conversely, having a kitchen reduces the daily cost by more than $28. See [Analysis of Features](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#analysis-of-features) section for more.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/57772a6c-a902-4b33-9d97-327cc9234be2)

The web application was built using [StreamLit](https://victoriadata606-nbrfse7xgiopgqdvdap4jy.streamlit.app/). The user interface looks like the below. It allows the user to enter the details of the Airbnb and calculate a daily price.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/376bde96-d4a4-46ed-815b-df6d1acb8d69)


## Conclusion

### Interpretation of Results

#### Analysis of Features
The final 14 features revealed some interesting discoveries about Airbnb pricing. Number of reviews in the last 12 months (1) is the most important feature for predicting price. It marries quantity *and* quality of reviews, as guests who view the listing after it has received high praise, are more likely to book that bnb and in turn, leave another high review (this assumes that all or most guests leave a review). It is somewhat related to the availability in the next 30 days (6) feature. These are the only features that give an indication of how often a bnb is booked. If a bnb is booked more often, likely it is highly rated and priced more accurately for its value than listings that are not booked as often. Number of bedrooms (2), number of people the bnb accommodates (3), and number of bathrooms (7) are not as surprising. These are typical property attributes that can indicate size and luxury of the Airbnb. The bigger the size, the higher the price. Location rating (4) is curiously high in importance which points to convenience being an important factor in how expensive an Airbnb is. For Airbnbs in New York City, a primarily walking and public transportation city, location is key. Room type (5) is another expected contributor to price. If the entire apartment is offered, it will be more desirable than a private room which will be more desirable than a shared room. Location in terms of the borough the property is located in is also a high contributor. Because location is a one-hot encoded feature, the interpretation is a bnb price changes by the dollar amount of the coefficient. In other words, a Manhattan (8) bnb is associated with a $32.44 increase in price according to the linear regression model. Similarly, if it's in Queens (13) or the Bronx (14), it is associated with a *decrease* in price of $19.14 and $28.42 respectively. As for amenities, having a washer (9) was most impactful to price. Having a washer in NYC is relatively rare and would speak to the luxury of the bnb. Having a TV (10) might indicate a larger bnb that could accommodate the wall space. The most surprising, though, is that mentioning 'kitchen' (12) in the amenities contributed to a *decrease* in price by $18.42. This could be due to entire homes/apartments not needing to specify a kitchen and that only private and shared rooms would need to explicitly state accessibility to a kitchen resulting in a lower price when it is mentioned. Accessibility (11) has the smallest impact, but was kept because contributed to successfully meeting the under $50/day error target. Also, the distance to public transportation was an interesting addition that will be enhanced in the future (see [Future Research](https://github.com/vicotriangle/victoria_data606/blob/main/docs/report.md#future-research) section below).

| Rank  | Name | Coefficient |
| ------------- | ------------- |------------- |
| 1| number_of_reviews_ltm  | 216.93  |
| 2 | bedrooms  | 206.75  |
| 3  | accommodates  |149.60  |
| 4 | review_scores_location  |116.08  |
| 5  | room_type  |87.69  |
| 6  | availability_30  |62.47  |
| 7 | new_bathroom  |51.02  |
| 8  | borough_Manhattan  |32.44  |
| 9  | Washer  |15.22  |
| 10  | TV  |12.91  |
| 11  | accessibility  |9.04  |
| 12  | Kitchen  |-18.36  |
| 13  | borough_Queens  |-19.14  |
| 14  | borough_Bronx  |-28.42  |

#### Analysis of Machine Learning Models
Throughout the process of refining the final dataset and features, the three machine learning models were analyzed to assess the impact of each change. To optimize the model, there must be a balance between enough features that do not correlate with each other to produce a reasonable accuracy, and minimizing the feature count to have good performance of the model. If the change improved the model, it was kept. If it worsened the model without minimizing features or rectifying multi-collinearity, it was rolled back. The table below shows the RMSE of each regression model at each phase of the execution performed. At every step, the LGBM regression model out-performs the polynomial regression model which out-performs the linear regression model. After step 1, accuracy decreased by about $6 for the LGBM model because of the removal of highly correlated features. However, the feature count went from 30 to 11, which is a desirable trade-off. Likewise, feature selection at step 4 reduced features from 21 to 13 to remove fields that did not contribute to the model significantly. At the final step, accessibility improved the model minimally, but reduced error to under $50 per day, which is a respectable result for the first version of this project.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/9ea900da-e016-4132-94cd-c3c306536eca)


#### Analysis of Deployment Application
For the StreamLit app, accuracy is at 57.69. Although it is quite a bit less accurate than the higher-feature models that were refined in this project, the tool must sacrifice some of it's performance for user-friendliness. In addition, there was functionality in StreamLit that did not work. A user should be able to create a requirements.txt file in GitHub that contains the imports for the functions used in the desired model. A JSON of the model was successfully exported in Python and uploaded to GitHub, but because StreamLit was unable to process the necessary package imports, this step failed. For that reason, a simple linear regression model was used by brute-force calculation of price using coefficients. The tool was also created so that the information it requests is easily obtainable by a host. If the tool requires information that is not intuitive or cannot be retrieved on the fly by the Airbnb host, usability is reduced and the tool is not providing the service as intended. These more nuanced data points include the number of reviews the listing received in the last 12 months, the review rating of location, and the availability in the next 30 days. Easier information to produce is borough the Airbnb is located in, overall rating, typical listing data, and amenities it offers. The tool was a success based on easy of use, user-friendliness, style, and output.

### Learnings
This project was a successful learning experience. On the surface, the full lifecyle of discovery to deployment of a project using machine learning has greatly enhanced my skillset and knowledge. This includes in the areas of:
1. Understanding whether a dataset is usable
   - This dataset was excessively right-skewed. Because of this, there were challenges in visualizing the data. Using density charts was much more effective in understanding features than boxplots, scatter charts, and histograms.
3. Data preparation
   - Sklearn's label encoder shortcut made it easy to assign consecutive numbers to categorical values that did not have ordinality.
   - Understanding when it is appropriate to use which type of encodings (label encode, custom encode, one-hot encode)
   - Assessing whether a change in the dataset would improve the model was done using linear refgression RMSE excessively in order to produce the best result to be entered into the final regression model. Improvement occurred when Airbnbs in NJ and Staten Island were removed, interquartile method was used on price to eliminate outliers, amenities were added, feature selection was performed on amenities, and when supplemental data was added (station locations). The model worsened when all data was removed except Manhattan, ratings of 0, price of 0, and listings with less than 3 reviews were included. It also did not help the model to reduce the outliers any further than 1.5x the interquartile range, which was interesting.
   - It was the first time I used Natural Language Processing effectively in a project. Using NLP to parse through 3,800 amenities to identify the most frequent options was a value add to the final product.
4. Machine learning techniques
   - Using LazyPredict made it trivial to choose the best machine learning model. I knew I wanted to use linear regression to understand feature importance, and polynomial regression based on the results of the linear regression displaying polynomial patterns. It was the first time I used LazyPredict to identify the best model for a project.
   - LGBM Regression model was the best model result from LazyPredict and the one I used.
5. Streamlit, VSCode, and GitHub
   - It was my first time using GitHub to manage project files, edit .md files in markdown, and fork to our class's repository.
   - Using VSCode was a new skill I needed for the development step of the StreamLit application. On running the code in VSCode, the user interface on a local instance of the browser would refresh and display the StreamLit tool I built.
   - It was also my first time using StreamLit. This is a powerful application and was awesome to see my project come to life in a public user interface. It pulls code straight from my GitHub repository.
6. Google Maps API
   - For calculating the distance between Airbnbs and subway stations, initially I used the Google Maps API. This was a cool implementation in Python and process to learn. It enabled the addition of an accurate walking distance straight from Google Maps as a guest would use to navigate to the nearest subway. However, the Google Map API is only free for a trial period. The volume of API calls needed for this project was high and I made the mistake of running the entire dataset through the API several times before I realized I was racking up a near $1,000 bill from Google. In the future, I will use smaller sample data sets to refine the code needed, and only run the entire code once, after all the code was perfected.
7. Real Estate data
   - Real estate prices are somewhat influenced by the "eye of the beholder" effect. There may be a large range of prices that would be acceptable as a daily cost for an Airbnb. This will trend strongly with value, but understanding that even the best fit model for real estate prices will never have an impressively low error is helpful in interpreting this project's results. What is a good value for one person is subjective and may be different from another.
   - In researching other machine learning projects using Airbnb data, I found that this dataset is missing key features that would have improved the performance significantly. The only features offered that gave an indication of popularity of the Airbnb were the future availability columns and the number of reviews in the past specified time frame columns. Other projects had booking rates which explicitly illustrated "out of how many days an Airbnb is available to book, how much of that time is it booked?". They also had features that gave a measure of grandeur including square footage, whether it boasted a desirable view, what floor the home was on, and other esthetics. This data enabled other data scientists to reduce their errors to around $20 per day and would have been helpful to include in this dataset.
  


### Future Research
There are a lot of elements of this project worthy of more research to optimize the web application product.
1. Data
   - Re-enable Google Maps API to get a more accurate walking distance calculation and see how it improves the model.
   - Get additional Airbnb data that proved important to similar projects including booking rate, square footage, quality of view, floor, and esthetics.
   - Unknowns in price such as cleaning fees, admin fees, and processing fees were not included in this analysis. These may affect valuation of Airbnbs because these additions can be very high.
   - Get data scrapes of Airbnb weekly to have results that are constantly up to date.
   - Research more into the meaning behind the feature importance found in this project. This understanding can be passed to hosts so they can enhance their Airbnb investment.
2. StreamLit
   - Implement LGBM Regression model in StreamLit. This didn't work for the first version of the tool, but will produce more accurate pricing.
   - Add more transparency to the tool including a section or file attachment that breaks down what features are most important and why so the host will be able to use that information to their advantage.
   - Add a display of other comparable homes that can be analyzed by the host upon submitting the StreamLit form. This will help them understand how competitive their price is.
   - Add in market influencers as toggles to give the investors even more information about what their listing is worth in the current market.
   - Allow host to choose their investment strategy from competitive to aggressive so they can tailor their investment management approach directly. Or, have the tool offer a range of prices that would be fit for the Airbnb from competitive to aggressive.
   - Enhance the tool with reading materials and references so hosts have a full picture of every component of their listing that is affecting their bottom line.



