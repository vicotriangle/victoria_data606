# Using Machine Learning to Analyze Airbnb Prices

**Author** Victoria Borsetti \
**Course** DATA 606: Capstone in Data Science \
**Term** Summer 2023

![image](https://github.com/vicotriangle/victoria_data606/assets/135077759/acff7126-38cb-4d52-b7af-68f4a96e62e7)






## Preliminary EDA Results
The preliminary analysis of the data confirmed that this data is interesting and usable. The first check done was to look at the frequency of column nulls. In general, the listings data was highly populated which is a good sign. The reviews dataset was missing only about 200 out of almost 1 million rows. These 200 were removed to be diligent about clean data. Datatypes were changed as appropriate for the columns that were imported in an unusable format. For example, price was a string that included a "$" that needed to be fixed. The dollar sign was removed, and the column was converted to a float which will make it usable later. There was one column "bathrooms" that contained no data, but it was discovered that column "bathroom text" contained the number of bathrooms and the bathroom type of "private" or "shared". This column was used to extract the number of bathrooms for later usability.
Standard statistics were taken for every numerical column. Some of the fields including accommodates, host listings count, and beds had dramatic outliers. When travelers rated their stays, the attribute with the largest standard deviation was cleanliness. Also, by looking at correlation data, it was found that travelers' rating of value of the experience was the highest predictor of overall rating. No other correlations were terribly helpful in that they accurately trended with price or ratings.
A heat map was made on a scatter plot of ratings versus prices to understand their distribution and density. It was found that listings with a price of just under $100 and a rating of 5.0 were the most common. the data was cleaned up to include only the middle 80% of prices and the top 75% of ratings.
Histograms were then created to understand the resulting distribution after data was cleaned. This was used to confirm that the data is relatively clean and ready to be used.


## Challenges:
1. Importing the data directly from Google Drive is not working. A workaround was created so that the script will download the file properly from Google Drive to the user's local drive before it is loaded into the Python kernel. This may need to be fixed.
2. Translating the reviews that were not in English did not work. Needs more research into the impact of not translating or another solution.
