from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import json
import re

consumer_key = '7jfGCb9GU7A63IMrmEhFxTDkR'
consumer_secret = 'AljFCAutO5VXSXeehMNsPJUEVyKJbKGuwe7oIvyK61yOvf0amr'
access_token = '831373652931334144-uAm36GTJqYlAYSck2dPeqpFfVvggQcS'
access_token_secret = 'u2KHnspQGLlc7yO9iW8ohiCfrDXqBAoEaDT9xe9VM3EMt'

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

if __name__ == "__main__":
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets = str(api.user_timeline(screen_name="ReallySwara", count=1))
    print(tweets)
    with open(r"C:\Users\Harsh Mistry\Documents\Twitter Personality analysis\data.json",'w') as outfile:
        json.dump(tweets,outfile)
    #twt = re.findall(r'\b#\w+',tweets)
    
    