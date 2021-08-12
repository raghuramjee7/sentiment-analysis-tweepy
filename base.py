import tweepy
import json
import re
import textblob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class SentimentEngine():

    def __init__(self, query):
        self.query = query
    
    def analyse_sentiment(self):
        self.get_tweets()

    def get_tweets(self):

        # Get the recent 100 tweets which contain our query topic

        tweet_cursor = tweepy.Cursor(api.search, q = self.query, lang = "en", tweet_mode = 'extended', include_rts = False).items(100)
        tweets = [tweet.full_text for tweet in tweet_cursor]

        # Creates a dataframe of the tweets

        tweets_df = pd.DataFrame(tweets, columns = ['Tweets'])

        self.clean_data(tweets_df)

    def clean_data(self, tweets_df):
        
        # uses regular expressions to remove
        # unwanted things like hashtags, mentions, urls

        for _,row in tweets_df.iterrows():
            row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
            row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
            row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
            row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
            row['Tweets'] = re.sub('\\n', '', row['Tweets'])

        self.find_polarity(tweets_df)
    
    def find_polarity(self, tweets_df):

        # uses the textblob library to fine the 
        # polarity of each tweet
        # postive > 0 , negative < 0, neutral = 0

        tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
        tweets_df['Result'] = tweets_df['Polarity'].map(lambda polarity: 'pos' if polarity>0 else 'neg')

        positive = tweets_df[tweets_df.Result == 'pos'].count()['Tweets']
        negative = tweets_df[tweets_df.Result == 'neg'].count()['Tweets']

        self.plot_graph(positive, negative)

    def plot_graph(self, positive, negative):

        # Plots the graph as per the sentiment
        
        plt.bar([0,1], [positive, negative], label = ["Positive", "Negative"], color = ["green", "red"])

        plt.legend()
        plt.show()

        


# -------------- API ACCESS KEYS ------------------

filename = 'keys.json'
with open(filename) as file_object:
    keys = json.load(file_object)

api_key = keys["api_key"]
api_key_secret = keys["api_key_secret"]

access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

# Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# --------------------------------------------------


# --- code begins here ------

if __name__=='__main__':

    query = input("Enter the topic you wanna analyse: ")

    Engine = SentimentEngine(query)
    Engine.analyse_sentiment()