import tweepy
from textblob import TextBlob

consumer_key = "J7LMZpKQsfawkqmRAta7Uky5q"
consumer_secret="2WPJ5658c1vutR472rOp2qYFKQ7EB5D33Gf1Dl2WxxE2BDGM5X"

access_token = "4221407893-oFVXrYEMfIbHQj5Coarzrsoc2M9M86NaJ9NkNsE"
access_token_secret="7A0VNc7XzPKYHGnEyYg5mSdgLXMdMvPZdHcvUlp64gUBt"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

public_tweets= api.search("Modi")


for tweet in public_tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
