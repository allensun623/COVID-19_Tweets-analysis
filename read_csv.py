import numpy as np 
import pandas as pd

from pathlib import Path
import time

from settings import token
from settings import us_states
from settings import states
from settings import states_abb_dic
from settings import states_full_dic
# data preprocessing
from string import punctuation
from nltk.corpus import stopwords
# sentiment 
from textblob import TextBlob

def main():
    start = time.time()
    iterate_dir()
    stop = time.time()
    print("================================================================")
    print("Run time: %f" % (stop-start))


def iterate_dir():
    """
    Iterate jsonl files in each directory
    """
    data_dirs = ['csv/2020-01']
    for data_dir in data_dirs:
        count_files = 1
        # create a df to store info of cols for each month
        cols = ['id_str', 'created_at', 'state', 'sentiment', 'text_clean']
        df_month = pd.DataFrame(columns = cols)
        # list of csv file in current directory
        csv_list = list(Path(data_dir).glob('**/*.csv'))
        for path in csv_list:
            print("================================================================")
            print("Extracting at file %i out of %i" % (count_files, len(csv_list)))
            print(path)
            df = read_csv(path, cols)
            df_month = pd.concat([df_month, df])
            count_files += 1 

        with open(str(data_dir+'.csv'), 'w') as f:
            df_month.to_csv(f, index=False, encoding='utf-8') 


def read_csv(path, cols):    
    df = pd.read_csv(path)
    df = data_prepross(df)
    df = sentiment_analysis(df)
    df = df[cols]
    return df

def data_prepross(df):    
    # Data preprocess
    # Transform string data and remove punctuation and stop words
    df['text_clean'] = df['text']
    # lower case
    df['text_clean'] = df['text_clean'].apply(lambda x: str(x).lower())
    # remove punctuation
    df['text_clean'] = df['text_clean'].apply(lambda x: x.translate(str.maketrans('', '', punctuation)))
    # remove stop words
    nltk_stop = stopwords.words('english')                                          
    df['text_clean'] = df['text_clean'].apply(lambda x: ' '.join([c for c in x.split() if c not in nltk_stop])) 

    return df

def sentiment_analysis(df):
    # Sentiment analysis
    # TextBlob stands on the giant shoulders of NLTK and pattern, and plays nicely with both.
    # Here, we only extract polarity as it indicates the sentiment 
    # as value nearer to 1 means a positive sentiment 
    # values nearer to -1 means a negative sentiment. 
    # This can also work as a feature for building a machine learning model.
    df['sentiment_score'] = df['text_clean'].apply(lambda x: TextBlob(x).sentiment[0])
    df['sentiment'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
    df['sentiment_category'] = df['sentiment_score'].apply(lambda x: 1 if x > 0 else 2 if x < 0 else 0)

    return df




if __name__ == '__main__':
    main()