# Using Machine Learning to Analyze Airbnb Prices

**Author:** Victoria Borsetti \
**Course:** Capstone in Data Science \
**Term:** Summer 2023

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/acff7126-38cb-4d52-b7af-68f4a96e62e7)

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

  - Airbnb data comes from Kaggle at the link: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv
  - Column descriptions can be found at the link: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596

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
The hypothesis behind additional data is that an attribute that quantifies convenience of location of an Airbnb may affect daily price. Subway station location data is available through the NYC Metropolitan Transportation Authority. Calculating distance to the nearest station may contribute to a more accurate model.

  - Stations data can be found at the link: https://data.ny.gov/widgets/i9wp-a4ja

The file from New York City Stations Database is 457kB and includes 1.8k records and 34 fields. The only fields used in this project are longitude and latitude of station entrances so they can be compared to longitudes and latitudes of each Airbnb.

### Approach
All code, documents, and presentations will be published to Github: https://github.com/vicotriangle/victoria_data606/blob/main/. Python will be used for data exploration and model development through Google Colab (.ipynb). Streamlit will be used to create the user interface for the webapp, VSCode for editing, and GitHub as the deployment source for StreamLit.
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
4. Borough was one-hot encoded because there is no ordinality of the values, yet there is a low quanity of unique options. This added 4 new fields to the dataset, one for each borough. If the Airbnb is in that borough, the corresponding column will be "1" and "0" if not. This approach returned better results than using label encoding.
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
Following the observation that location rating was an important feature to determining price, it is now even more convincing that subway station data may enhance the model even further. A new dataset was added to the notebook to pull in longitude and latitude of subway station entrances. The map of the subway stations confirms that it will span appropriately to all of the Airbnb locations.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/301ee906-ba59-4632-8cec-392b0e0424d0)


Two columns were added to the Airbnb dataset. 'Distance', which will be the distance in feet from the Airbnb to the nearest subway station, and 'accessibility' which will be a flag that is 1 if the closest station is within 2,000ft and 0 if not. 2,000ft was found to be the distance that most improved the model while testing between 500ft and 5,000ft. This is logical, as 2,000 is approximately 3 blocks in NYC terms.
Cdist is a function that takes two sets of longitude and latitude arrays and calculates the distances between every set of points. This can be used to identify the shortest distance for each Airbnb and inserting it into the new 'distance' column. 'Accessibility' is then calculated based on this distance. Between both new columns, 'accessibility' was found to improve the model on its own more. Therefore, 'distance' was removed to avoid overfitting.

##### Final Features

After feature selection and addition of distance, these were the features that influenced price the most and their importance. The most important feature is the number of reviews the Airbnb received in the past 12 months. This is not too surprising. This is the only feature that gives an indication of how often a bnb is booked. The more a bnb is booked, the better the experience likely was for the guest, the higher the rating, and therefore, the higher the price. Number of bedrooms and number of people the bnb accommodates are also not surprising. Location rating is an interesting  4th feature that points to convenience being an important factor in how expensive an Airbnb is.

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

With these features, the importance of each changes from the original regression model. The most important attribute is whether the property is in Manhattan or not. If so, there is a $37 gain on the daily cost. Conversely, having a kitchen reduces the daily cost by more than $28. This is surprising, but may be because those that mention "kitchen" in their amenities are not offering an entire home/apartment and it is just a private room. In this case, having to specify a kitchen results in lower price as would be expected for a property offering just a private room.

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/57772a6c-a902-4b33-9d97-327cc9234be2)

The StreamLit application is accessible at the link: https://victoriadata606-nbrfse7xgiopgqdvdap4jy.streamlit.app/

The user interface looks like this. It allows the user to enter the details of the Airbnb and calculate a daily price.
![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/376bde96-d4a4-46ed-815b-df6d1acb8d69)


