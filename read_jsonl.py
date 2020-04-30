import json
import jsonlines
import numpy as np 
import pandas as pd

from pathlib import Path

from settings import token
from settings import us_states
from settings import states
from settings import states_abb_dic
from settings import states_full_dic

import time

def main():
    start = time.time()
    iterate_dir()
    stop = time.time()
    print("Run time: %f" % (stop-start))


def iterate_dir():
    """
    Iterate jsonl files in each directory
    """
    data_dirs = ['jsonl/2020-01']
    for data_dir in data_dirs:
        count_files = 1
        jsonl_list = list(Path(data_dir).glob('**/*.jsonl'))
        for path in jsonl_list:
            print("================================================================")
            print("Extracting at file %i out of %i" % (count_files, len(jsonl_list)))
            print(path)
            read_jsonl(path)
            count_files += 1   

def read_jsonl(file_name):
    """
    read a single jsonl file and extrac cols from each tweet 
    store as datafram in a csv file 
    """

    #columns of the csv file
    cols = ['id_str', # user id
            'created_at', # tweet created time
            'location', # location
            'state_abb', # abbreviation of state
            'state',
            'hashtags', 
            'text']
    # initial entry dictionary for every page
    new_entry = {i:[] for i in cols}
    count_tweets = 0

    with jsonlines.open(file_name) as f:
        for status in f.iter():
            # collect location in USA
            location = status['user']['location']
            if location == None:
                continue
            # location forms included in us_state in settings
            elif location.split(' ')[-1] not in us_states:
                continue
            # extract abbreviation of state and state from location
            state_abb, state = is_state(location)
            # printing the full text stored inside the tweet object
            try:
                text = status['retweeted_status']['full_text']
            except:  # Not a Retweet
                text = status['full_text']
            id_str = status['id_str']
            created_at = status['created_at']
            hashtags = ", ".join([t['text'] for t in status['entities']['hashtags'] if len(t) > 0])
            # print("====================================================")
            # print("id_str: %s" % id_str)
            # print("created_at: %s" % created_at)
            # print("location: %s" % location)
            # print("state: %s" % state)
            # print("state abbreviation: %s" % state_abb)
            # print("hashtags: %s" % hashtags)
            # print("=======text: \n %s" % text)
            new_entry['id_str'].append(id_str)
            new_entry['created_at'].append(created_at)
            new_entry['location'].append(location)
            new_entry['state_abb'].append(state_abb)
            new_entry['state'].append(state)
            new_entry['hashtags'].append(hashtags)
            new_entry['text'].append(text)
            count_tweets += 1
            # create a dataframe to add data from current page into it
    df = pd.DataFrame(data=new_entry) 
    file_path_name = str(file_name) + '.csv'
    with open(file_path_name, 'w') as f:
        df.to_csv(f, columns=cols, index=False, encoding='utf-8')
   
    print("US tweets: %i" % count_tweets)

def is_state(x):
    # return state name and its abbreviation
    for s in x.split(', '):
        if s in states:
            if s in states_abb_dic:
                return s, states_abb_dic[s]
            else: 
                return states_full_dic[s], s
                
    for s in x.split(' '):
        if s in states:
            if s in states_abb_dic:
                return s, states_abb_dic[s]
            else: 
                return states_full_dic[s], s

    return np.nan, np.nan



if __name__ == '__main__':
    main()