import tweepy
import json

# twitter keys
consumer_key = 'x9kB13vG4j6CtIwszEyhgAcy4'
consumer_secret = 'UlFnGcCaOqqx2cx4ZMQkvsRaSTN96Yoq4T1Yh7rp8GR8IdJiiv'
access_token = '761026063-t0XoJsd5brAYmVXvV8GnHzTQUAH8grpz2HAx0o6S'
access_token_secret = '0aggjvCPqAO5jCSVTOStrpAT3sB5NyzeKTio3EMJR2h6m'

# auth tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

my_tweets = api.user_timeline()

for tweet in my_tweets:
    print(json.dumps(tweet, sort_keys=True, indent=4, separators = (',', ': ')))