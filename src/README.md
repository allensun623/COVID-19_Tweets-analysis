# COVID-19_Tweets-analysis
In case any other team member has pushed new changes ahead, please check **`git status`**, and do **`git pull`** if necessary every time before you want to make some changes.

## Priority
Data CSV files in **[src](https://github.com/AllenSun7/COVID-19_Tweets-analysis/tree/master/src)**

### 1. **[us_sentiments_analysis.csv](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/us_case_tweet_sentiment_analysis.csv)**

This is for daily sentiment 
- sentiment range [-1, 1]
- Sentiment classification with **TextBlob**
    - Negative score [-1,0)
    - Neutral  score   0
    - Positive score (0,1]

### 2. **[us_cases_analysis.csv](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/us_case_analysis.csv)**

- This is for cases

### 3. **[us_tweets_analysis.csv](https://github.com/AllenSun7/COVID-19_Tweets-analysis/blob/master/src/us_tweet_analysis.csv)**

- This is for tweets analysis.
- They are accumulated tweets for each state

### us_case_tweet_sentiment_analysis.csv
- It conbines three files above