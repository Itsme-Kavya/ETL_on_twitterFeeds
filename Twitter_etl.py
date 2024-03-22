import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


access_key = "FIYWpeIWTHcSJoT7za0kZtNMi"
access_secret = "bd3wP64Gi2vcfxF8UKZMlpNz4gPX9fR9KftgWZ3XZpEutEXUo1"
consumer_key = "1771042776987189248-T6oIatx8rG97rTGtV2Pj5bJhPrQl9X"
consumer_secret = "YtSVfpqk4iWO0vOeKW01RssNrVXMH6KvKLq0OgMNfHnGs"


# authentication for access
#authorization= tweepy.OAuthHandler(access_key,access_secret)
#authorization.set_access_token(consumer_key, consumer_secret)

bearer_token = "AAAAAAAAAAAAAAAAAAAAAFjBswEAAAAAMLsp%2FJemH7GeBETwFYIPHP5y9HY%3DuKJLGhJffm8c7TyGtCojkXPe1JTDwRrpMWLQOg1SpFZAVVJYdy"
auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)

#API object
#api = tweepy.API(authorization)
api = tweepy.API(auth)
#extracting tweets
tweets = api.user_timeline(screen_name='@NVIDIAAI',
                           # num of tweets to extract
                           count = 100,
                           include_rts = False, 
                           # no retweets
                           # for full length of tweet
                           tweet_mode = 'extended'
                           )

print(tweets)
