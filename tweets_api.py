import tweepy
from settings import tokens

def my_info():
    """
    Example 1: Your Timeline
    """


    # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
    public_tweets = api.home_timeline()
    # foreach through all tweets pulled
    for tweet in public_tweets:
       # printing the text stored inside the tweet object
       print(tweet.text)
       print(tweet.user.screen_name)
       print(tweet.user.location)


def specifit_user(api):
    """
    Example 2: Tweets from a Specific User
    """

    # The Twitter user who we want to get tweets from
    name = "nytimes"
    # Number of tweets to pull
    tweetCount = 20
    # Calling the user_timeline function with our parameters
    results = api.user_timeline(id=name, count=tweetCount)
    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.text)
        print(tweet.user.screen_name)
        print(tweet.user.location)

def keywords(api):
    """
    Example 3: Finding Tweets Using a Keyword
    """

    # The search term you want to find
    query = "COVID-19"
    # Language code (follows ISO 639-1 standards)
    language = "en"
    count = 0
    num_count = 0
    pages=15
    # # Calling the user_timeline function with our parameters
    # results = api.search(
    #     q=query, 
    #     count=200,
    # )
    count_pages = 0
    results = tweepy.Cursor(api.search, q=query, count=100, lang='en', include_rts=False, wait_on_rate_limit=True)        # foreach through all tweets pulled
    for page in results.pages():
        for tweet in page:
            count += 1
            print("====================================================")
            # printing the text stored inside the tweet object
            print(tweet.text)
            print(tweet.user.screen_name)
            print(tweet.user.location)
            print(tweet.created_at)
            print(tweet.coordinates)
            # print(tweet)
        count_pages += 1
        print("At page: %i" % count_pages)
        print("Total tweets so far: %i" % count)

    print(count)

def main():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
    # Setting your access token and secret
    auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)

    keywords(api)


if __name__ == '__main__':
    main()
























