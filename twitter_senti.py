import tweepy
from textblob import TextBlob

consumer_key = "insert here"
consumer_secret="insert here"

access_token = "insert here"
access_token_secret="insert here"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

public_tweets= api.search("Modi")


for tweet in public_tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
