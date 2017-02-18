import re
import tweepy
from textblob import TextBlob


class MovieSentimentAnalysis(object):

    def __init__(self):

        # keys and tokens from the Twitter Dev Console
        consumer_key = 'dddacgOCMuZlhJJY4oVxEV0MKQ'
        consumer_secret = 'zz9apw9qrSrIwUIsPftHxCEyaWBlCSCkp7DpnaU7EpnCFSYG30A'
        access_token = '8863018473-JoVCOaAEhFLjLEBLtyy66Bi3i2uW56KA5xQsfIYq'
        access_token_secret = 'FFDOkhF19CEWearnOa9TOr09Jp4e0u4AYD06pbjqCk21QN'

        # attempt authentication
        try:
            # create OAuthHandler object
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(auth)
        except:
            print("Error: Authentication Failed")

    def search_movie_tweets(self):

        # Search for your movie name on Twitter
        self.public_tweets = self.api.search(q='moana', count=200)

    def analyze_tweets(self):

        # Define a threshold for each sentiment to classify each
        for tweet in self.public_tweets:
            tweetText = self.clean_tweet(tweet.text)
            analysis = TextBlob(tweetText)
            print(tweetText)
            print(analysis.sentiment)

    def clean_tweet(self, tweet):

        # Utility function to clean tweet text by removing links, special charactersusing simple regex statements.
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

def main():

    obj = MovieSentimentAnalysis()
    obj.search_movie_tweets()
    obj.analyze_tweets()


if __name__ == "__main__":
    main()