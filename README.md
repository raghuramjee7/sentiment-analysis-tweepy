# Sentiment Analysis Engine

A Sentiment analysis engine that fetches tweets using the Twitter API and Tweepy library and applies NLP on them to find the sentiment using textblob library and plots its positive and negative sentiment histogram. It takes a keyword as the input and fetches 100 tweets containing that topic, cleans the tweets and feeds them to the textblob library, which assigns a polarity value to them and then plots a histogram of positive vs negative sentiment.

## How to run

* Clone the repository in your local system.
* Install the required python libraries in your local machine - tweepy, textblob, pandas, matplotlib.
* Get your API keys from the Twitter Developer Plaftorm and paste them in the json file.
* Run the base.py file using `python base.py` by moving to the directory.
* Input the topic you want to analyse sentiment on.
