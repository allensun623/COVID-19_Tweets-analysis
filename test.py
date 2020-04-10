import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re #regular expression
from textblob import TextBlob
import string
import preprocessor as p
from settings import tokens


def info(api):
    # 5. Create file paths for the 3 CSV files
    #declare file paths as follows for three files
    telemedicine_tweets = "telemedicine_data.csv"
    epilepsy_tweets = "epilepsy_data.csv"
    heart_stroke_tweets = "heart_stroke_tweets_data.csv"

    # 6. What exactly we need to extract?
    # columns of the csv file
    COLS = ['id', 
            'created_at', 
            'source', 
            'original_text',
            'clean_text', 
            'sentiment',
            'polarity',
            'subjectivity', 
            'lang',
            'favorite_count', 
            'retweet_count',   
            'original_author',   
            'possibly_sensitive', 
            'hashtags',
            'user_mentions', 
            'place', 
            'place_coord_boundaries']

    # 7. Handle Emoticons and Emojis
    #HappyEmoticons
    emoticons_happy = set([
        ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
        ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
        '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
        'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
        '<3'
        ])
    # Sad Emoticons
    emoticons_sad = set([
        ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
        ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
        ':c', ':{', '>:\\', ';('
        ])
    # 7.2 Emoji Recognition
    #Emoji patterns
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
    # And then we combine both happy and sad emoticon array-lists first:
    #combine sad and happy emoticons
    emoticons = emoticons_happy.union(emoticons_sad)

    # 8. Method to Clean (Preprocessor)

    # 9. Extract Tweets

    # 9.1 Beginning of the method
    def write_tweets(keyword, file):
        #If the file exists, then read the existing data from the CSV file.
        if os.path.exists(file):
            df = pd.read_csv(file, header=0)
        else:
            df = pd.DataFrame(columns=COLS)
        #page attribute in tweepy.cursor and iteration
        for page in tweepy.Cursor(api.search, q=keyword, count=200, include_rts=False):
            # 9.2 JSON
            for status in page:
                new_entry = []
                status = status._json
            if status['lang'] != 'en':
                continue
            # 9.3 Replace RT’s and FAVs
            if status['created_at'] in df['created_at'].values:
                i = df.loc[df['created_at'] == status['created_at']].index[0]
                if status[‘favorite_count’] != df.at[i, ‘favorite_count’] or \
                    status[‘retweet_count’] != df.at[i, ‘retweet_count’]:
                    df.at[i, ‘favorite_count’] = status[‘favorite_count’]
                    df.at[i, ‘retweet_count’] = status[‘retweet_count’]
                    continue

    # 9.3 Replace RT’s and FAVs






def main():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
    # Setting your access token and secret
    auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    
    info(api)


if __name__ == '__main__':
    main()

