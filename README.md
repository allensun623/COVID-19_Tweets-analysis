# COVID-19_Tweets-analysis
In case any other team member has pushed new changes ahead, please check **`git status`**, and do **`git pull`** if necessary every time before you want to make some changes.

## Enviroment Setup
- (Python 2) Run `pip install -r requirements.txt`
- (Python 3) Run `pip3 install -r requirements.txt`

## Priority
Data CSV files in **[src](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/src)**

## 1. Tweets Collecting Tutorial
In the subfolder of **[tweets_collecting_tutorial](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/tweets_collection_tutorial)** 
- 1.1 Examples: there are three examples of collecting tweets:
    - Example 1: Your Timeline
    - Example 2: Tweets from a Specific User
    - Example 3: Finding Tweets Using a Keyword
- 1.2 Collect data   
    - 1.2.1 Set up API key
    - 1.2.2 Set up argument in main file


## 2. Data Analysis
### 2.1 Sentiment Analysis
There are sample datasets stored in the folder `tweets` for analysis collected on **4/21/2020**.

In the Jupyter Notebook file **[sentiment_analysis.ipynb](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/sentiment_analysis.ipynb)**:
- Data preprocessing 
    Text preprocessing technicks in the **[read_csv.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/read_csv.py)**
    - Lower case
    - Remove URL address
    - Remove Unicode
    - Remove stop words
    - Remove hashtag 
    - Remove integers
    - Remove emoticons
    - Remove punctuation

### Data Visualization
- Word Cloud
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/tweets_wordcloud.png"/>

- Heatmap
    - Tweets Heatmap 
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/heatmap_tweets.png"/>
    - Cases Heatmap
<img src="https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/heatmap_cases.png"/>

## Task Lists
- [ ]  1) automating the tweets collection.
- [ ]  2) finding co-relation between linear graph for cases and tweets for different states.

## Notes
- It took 3 hours to collect around 150K tweets, and the timeline showed that these tweets were posted within just past 1 hours. It means people are posting tweets much faster than we could collect. 
- What else infomation should we extract from a each single tweet? Above `cols` shows what we want to extract so far.
- Rate Limit.
    - wait_on_rate_limit. Whether or not to automatically wait for rate limits to replenish. Rate limits are divided into 15 minute intervals.  
    - Total Requests Limit. For each free API key, there is a limit for monthly requests: up tp 250. 