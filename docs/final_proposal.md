Victoria Borsetti

August 1, 2023

### Overview
Real Estate and travel are passions of mine. I frequently use accommodation services such as AirBnb, VRBO, Zillow, Realtor.com, etc. to explore, visit, and book properties all around the world. One thing that is an intriguing thought is that there must be a recipe that hosts of successful accommodations follow, or a pattern of attributes about properties, amenities, and overall experience that make those properties good candidates for renting out for short stays in a profitable way. This project attempts to understand what features of an Airbnb contribute to its daily price. The data being used for this project are details on AirBnb listings in New York City. Success will be measured using RMSE on the machine learning models. This can then be deployed as a tool that can assist Airbnb investors in pricing their listings in such a way that optimizes profits.


### Sources
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

  - [Subway Stations](https://data.ny.gov/widgets/i9wp-a4ja) data is made available by the state of NY

The file from New York City Stations Database is 457kB and includes 1.8k records and 34 fields. The only fields used in this project are longitude and latitude of station entrances so they can be compared to longitudes and latitudes of each Airbnb.

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
