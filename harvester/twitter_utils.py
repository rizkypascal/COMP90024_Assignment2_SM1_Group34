import json
import tweepy
import couchdb

class TwitterUtils:
    def client(self):
        with open("twitter_api_credential.json", "r") as f:
            credential = json.load(f)

        auth = tweepy.OAuthHandler(credential["api_key"], credential["api_secret"])
        auth.set_access_token(credential["access_token"], credential["access_token_secret"])
        return tweepy.API(auth, wait_on_rate_limit=True)
    def db(self):
        server = couchdb.Server("http://user:pass@127.0.0.1:15984")
        return server["testing"]
    