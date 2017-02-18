import tweepy
from textblob import TextBlob

# Step 1 - Insert your API keys
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'
access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 2 - Search for your movie name on Twitter
public_tweets = api.search('movie_name')

# Step 3 - Define a threshold for each sentiment to classify each
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

