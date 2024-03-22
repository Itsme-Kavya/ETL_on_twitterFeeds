import pandas as pd
from ntscraper import Nitter

# scrapping tweets from twitter
scraper = Nitter()

#extracting data from tweets
def extract_tweets(name, modes, n):
    tweets = scraper.get_tweets(name, mode=modes, number=n)
    FinalTweets = []
    for tweet in tweets['tweets']:
        data = [tweet['link'], tweet['text'], tweet['date'], tweet['stats']['likes'], tweet['stats']['comments'], tweet['stats']['retweets']]
        FinalTweets.append(data)

    TweetsData = pd.DataFrame(FinalTweets, columns=['link', 'content', 'date', 'likes', 'comments', 'Num_retweet'])
    return TweetsData

TweetsData = extract_tweets('RCBTweets', 'user', 5)
TweetsData