import tweepy as tw
import pandas as pd
import requests


bearer_token = "AAAAAAAAAAAAAAAAAAAAALUBiAEAAAAAo%2FxvPkzkTNiJXWvUlMCLqeKWHmA%3DTo30DOyGtEkyGL43kdCjr3uHstt0ISvOWwFL0hqhIeD8hK7pcY"
consumer_key= "3uELbUxSAXlZCbtz4ZJBoYkmr"
consumer_secret= "ggI6fDLOS8zrXqPDIrB8bBsXAVRGt84OjhnGyIQl8lkdkg4MoZ"
access_token="866689982492278785-7uDNqjI0RmuobYmgzpntoHV3hTh0XIv"
access_token_secret="hXoIM8ft5cJY9alQvJQsUTYCF1K6euUztXVlgUMgHAgJJ"

client = tw.Client(bearer_token=bearer_token,
                   consumer_key=consumer_key, 
                   consumer_secret=consumer_secret, 
                   access_token=access_token, 
                   access_token_secret=access_token_secret, 
                   return_type = requests.Response,
                   wait_on_rate_limit=True)
query = "#UChicago"
tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id', 'created_at'],
                                     max_results=100)
tweets_dict = tweets.json() 
tweets_data = tweets_dict['data'] 
df = pd.json_normalize(tweets_data) 
df.head(50)