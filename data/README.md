# Sources
This project utilizes two raw data sources from the web. The primary source is NYC Airbnb data from Kaggle. The supplemental source is subway station locations offered by NY.gov. To view this data and its source website, follow the links below in step ONE. To import the data into a python notebook, use the Google Drive codes in step TWO.

## Two options for viewing Airbnb and subway station location data:
1. View/download from original sources:
  - NYC Airbnb data from Kaggle: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc?select=listings+2.csv
      - Metadata: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596
  - Subway station location data from NY.gov: https://data.ny.gov/widgets/i9wp-a4ja
2. Import from my personal Google Drive using code given below


### Airbnb Data:
url = 'https://drive.google.com/file/d/1YU91bN5I9mIj75if3T12dVWbxNco95Wd/view?usp=drive_link' \
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2] #reformat

#define a dataframe called abnb0 containing all listing data. Specify the datatypes.

abnb0 = pd.read_csv(path, dtype={"listing_url": "string","scrape_id": "float","last_scraped": "string","name": "string",
                    "description": "string","neighborhood_overview": "string","picture_url": "string",
                    "host_id": "float","host_url": "string","host_name": "string","host_since": "string",
                    "host_location": "string","host_about": "string","host_response_time": "string",
                    "host_response_rate": "string","host_acceptance_rate": "string","host_is_superhost": "string",
                    "host_thumbnail_url": "string","host_picture_url": "string","host_neighbourhood": "string",
                    "host_listings_count": "float","host_total_listings_count": "float","host_verifications": "string",
                    "host_has_profile_pic": "string","host_identity_verified": "string","neighbourhood": "string",
                    "neighbourhood_cleansed": "string","neighbourhood_group_cleansed": "string","latitude": "float",
                    "longitude": "float","property_type": "string","room_type": "string","accommodates": "float",
                    "bathrooms": "float","bathrooms_text": "string","bedrooms": "float","beds": "float",
                    "amenities": "string","price": "string","minimum_nights": "float","maximum_nights": "float",
                    "minimum_minimum_nights": "float","maximum_minimum_nights": "float","minimum_maximum_nights": "float",
                    "maximum_maximum_nights": "float","minimum_nights_avg_ntm": "float","maximum_nights_avg_ntm": "float",
                    "calendar_updated": "string","has_availability": "string","availability_30": "int64",
                    "availability_60": "float","availability_90": "float","availability_365": "float",
                    "calendar_last_scraped": "string","number_of_reviews": "float","number_of_reviews_ltm": "float",
                    "number_of_reviews_l30d": "float","first_review": "string","last_review": "string",
                    "review_scores_rating": "float","review_scores_accuracy": "float",
                    "review_scores_cleanliness": "float","review_scores_checkin": "float",
                    "review_scores_communication": "float","review_scores_location": "float",
                    "review_scores_value": "float","license": "string","instant_bookable": "string",
                    "calculated_host_listings_count": "float","calculated_host_listings_count_entire_homes": "float",
                    "calculated_host_listings_count_private_rooms": "float",
                    "calculated_host_listings_count_shared_rooms": "float","reviews_per_month": "float"})


### Stations data:
url = 'https://drive.google.com/file/d/1AJAmcOmbzt5vHyaMltmw9GmIPZGx2lhq/view?usp=drive_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

#define a dataframe called stations containing ONLY longitude and latitude of all stations data.

stations = pd.read_csv(path, usecols = ['Entrance Latitude','Entrance Longitude'])
stations.columns = ['slat','slon']
stations.drop_duplicates(inplace=True) #remove duplicate stations (different entrances for same station)

