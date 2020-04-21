# COVID-19_Tweets-analysis
In case any other team member has pushed new changes ahead, please check **`git status`**, and do **`git pull`** if necessary every time before you want to make some changes.

## 1. TWEETS Collecting

### Examples
Under the file
**[tweets_api_eg.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/tweets_api_eg.py)**

There are three examples of collecting tweets:
- Example 1: Your Timeline
- Example 2: Tweets from a Specific User
- Example 3: Finding Tweets Using a Keyword

### Main class
- In the python file **[main.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/main.py)**, set parameters `api token`, `folder`, `file name`, and `keywords`. 

Run `main.py` to collect tweets with keywords.
```
# api token
api_token = token
# write in to file
file_name = 'tweets-covid-19.csv'
# folder to store your collected data
folder = 'test_data'
# search keyword
# 'COVID-19', 'COVID19', 'Covid_19', 'CoronavirusPandemic', 'CoronavirusOutbreak','CoronaVirusUpdate'
keywords = ['COVID']
```

- In the **[settings.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/settings.py)**, you can use your own token.

    - **[Twitter Data Mining: A Guide to Big Data Analytics Using Python](https://chatbotslife.com/twitter-data-mining-a-guide-to-big-data-analytics-using-python-4efc8ccfa219)** is a tutorial of how to apply for a developer ID and how to utilize it. 


- **[tweets_info.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/tweets_info.py)** is a Python class to collect tweets

    - Columns we will collect, change the `cols` in  `tweets_info.py` to get more information from each single tweet.
    ```
    #columns of the csv file
    cols = ['screen_name', # user id
            'created_at', # tweet created time
            'location', # location
            'source', # tweet source: phone, web, ...
            'hashtags', 
            'text']
    ```

## 2. Data Analysis
### 2.1 Sentiment Analysis
sample datasets are in the folder `tweets` for analysis collected on **4/21/2020**
In the Jupyter Notebook file `sentiment_analysis.ipynb`


## Notes
- It took 3 hours to collect around 150K tweets, and the timeline showed that these tweets were posted within just past 1 hours. It means people are posting tweets much faster than we could collect. 
- What else infomation should we extract from a each single tweet? Above `cols` shows what we want to extract so far.