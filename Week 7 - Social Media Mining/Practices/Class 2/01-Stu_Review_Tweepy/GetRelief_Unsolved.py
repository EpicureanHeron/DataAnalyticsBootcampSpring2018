# Dependencies
import tweepy
import json
import config

# TODO: move keys to config file and import from there
# twitter keys
# Twitter API Keys
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# auth tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User Account
target_user = "@Stress_tips123"

# Counter
counter = 0

# TODO: UNCOMMENT THE FOLLOWING BLOCK AND COMPLETE THE CODE
# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    user_tweets = api.user_timeline(target_user, page=x)

    # Loop through all tweets
    for tweet in user_tweets:

        # Utilize JSON dumps to generate a pretty-printed json
        #print(json.dumps(tweet['text'], sort_keys=True, indent=4, separators=(',', ': ')))

        # Print Tweets
        print(tweet['text'])


        # Add to Counter
        counter += 1

print(str(counter) + ' Tweets Printed')