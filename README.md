# COVID-19_Tweets-analysis

## tweets collecting

### Examples
under the file
**[tweets_api_eg.py](https://github.com/AllenSun7/CS229_Machine-Learning/tree/master/ex1-week2)**
There are three example of collect tweets
- Example 1: Your Timeline
- Example 2: Tweets from a Specific User
- Example 3: Finding Tweets Using a Keyword

### Main class
in the python file **[main.py](https://github.com/AllenSun7/CS229_Machine-Learning/tree/master/ex1-week2)**
in the **[settings.py](https://github.com/AllenSun7/CS229_Machine-Learning/tree/master/ex1-week2)**, use your own token 
**[Twitter Data Mining: A Guide to Big Data Analytics Using Python](https://chatbotslife.com/twitter-data-mining-a-guide-to-big-data-analytics-using-python-4efc8ccfa219)** is a tutorial of how to apply for a developer ID and how to utilize it. 


**[tweets_info.py](https://github.com/AllenSun7/CS229_Machine-Learning/tree/master/ex1-week2)** is class to collect tweets
columns we will collect, chang the `cols` in  `tweets_info.py` to get more information from each single tweet.
```
#columns of the csv file
cols = ['screen_name', # user id
        'created_at', # tweet created time
        'location', # location
        'source', # tweet source: phone, web, ...
        'hashtags', 
        'text']
```
