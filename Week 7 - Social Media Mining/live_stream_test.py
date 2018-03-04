import tweepy
import json
#override tweepy.StreamListener to add logic to on_status

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

# twitter keys
consumer_key = 'x9kB13vG4j6CtIwszEyhgAcy4'
consumer_secret = 'UlFnGcCaOqqx2cx4ZMQkvsRaSTN96Yoq4T1Yh7rp8GR8IdJiiv'
access_token = '761026063-t0XoJsd5brAYmVXvV8GnHzTQUAH8grpz2HAx0o6S'
access_token_secret = '0aggjvCPqAO5jCSVTOStrpAT3sB5NyzeKTio3EMJR2h6m'

# auth tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# set stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, listener=myStreamListener)

# set live tweets to variables

tweets.append(myStream.filter(track=['Trump']))

# create list
print(tweets)
