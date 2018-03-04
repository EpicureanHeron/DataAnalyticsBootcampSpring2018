# Dependencies
import tweepy
import time
import json
import config

# Twitter API Keys
# Twitter API Keys
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# Target Term
target_term = "@SouthWest"

# Opening message
print("We're going live, sir!")

# Create Thank You Function
def ThankYou():
    print('in func')
    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # TODO Search for all tweets
    public_tweets = api.search(target_term, count=5)
    # TODO Loop through all tweets
    print(len(public_tweets))
    for tweet in public_tweets['statuses']:
        # TODO Get ID and Author of most recent tweet directed to me
        tweet_id = tweet['id']
        tweet_author = tweet['user']['screen_name']
        tweet_text = tweet['text']

        # TODO Print the tweet_id
        print(tweet_id)
        print(tweet_author)
        print(tweet_text)
        # TODO Use Try-Except to avoid the duplicate error
        #try:
        # CODE HERE

            # Print success message
            # CODE HERE
        #except Exception:
        # CODE HERE

        # @TODO Print message to signify complete cycle
        # CODE HERE


# @TODO Set timer to run every minute
ThankYou()
