# COVID-19_Tweets-analysis
In case any other team member has pushed new changes ahead, please check **`git status`**, and do **`git pull`** if necessary every time before you want to make some changes.

## Enviroment Setup
- (Python 2) Run `pip install -r requirements.txt`
- (Python 3) Run `pip3 install -r requirements.txt`

## Priority
Data CSV files in **[src](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/src)**

## 1. Data Collection
### 1.1 Worldometer dataset
Run **[GetData_USA.py](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/Data_Collection/GetData_USA.py) to scripy the data from **[worldometers.info](worldometers.info)**
### 1.2 Tweets dataset
#### 1.2.1 General Tweets Collecting Tutorial
In the subfolder of **[tweets_collecting_tutorial](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/tweets_collection_tutorial)** 
- 1.1 Examples: there are three examples of collecting tweets:
    - Example 1: Your Timeline
    - Example 2: Tweets from a Specific User
    - Example 3: Finding Tweets Using a Keyword
- 1.2 Collect data   
    - 1.2.1 Set up API key
    - 1.2.2 Set up argument in main file

#### 1.2.2 Collect data 
Data was collected by filtering the original dataset under the repository of **[COVID-19-TweetIDs](https://github.com/echen102/COVID-19-TweetIDs)** which contains collected tweets IDs associated with the novel coronavirus COVID-19.
The original dataset contains Tweets’ ids dating from January 22th, 2020 to May 8th, 2020 with 101,718,655 tweets. Used the tool Hydrator to rehydrate the tweet-IDs i.e. to fetch tweets data related to the tweet-IDs using Twitter’s API. Filtered the location in the US only by the list in Appendix A. Extracted the attributes of id_str, created_at, location, and text of each tweet and features are categorical values following the steps below:
- 1. rehydrate the tweet-IDs and store them as .gz files.
- 2. Unzip the .gz files to .jsonl files
- 3. Extract relevant tweets and features from .jsonl files and store them as .csv files
- 4. Concatenate all .csv files into separate months.
Eventually, 15,099,967 tweets were collected, and the size of the dataset dropped from 1TB to 3GB. 
|Tweets Type            |Number of tweets   |Size of dataset  |
|-------------          |----------------   |---------------  |
| Original dataset      | 101,718,655       |   1 TB          |
| Filtered dataset      |  15,099,967       |   3 GB          |
| Preprocessed dataset  |  14,067,351       | 2.5 GB          |



## 2. Data Preprocess
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