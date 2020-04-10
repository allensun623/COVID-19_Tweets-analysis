from settings import token
from tweets_info import TweetsKeyword


def main():
    # api token
    api_token = token
    # write in to file
    file_name = 'tweets-covid-19.csv'
    # search keyword
    keywords = ['COVID-19', 'COVID19', 'coronavirus', 'coronaVirus']
    tweets = TweetsKeyword(api_token, file_name, keywords)
    tweets.collect_info()

if __name__ == '__main__':
    main()