import os
import json
import tweepy
import couchdb


class TwitterUtils:
    def load_config(self):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(curr_dir, "config.json")

        with open(config_file, "r") as f:
            credential = json.load(f)

        return credential


    def client(self):
        credential = self.load_config()
        auth = tweepy.OAuthHandler(credential["api_key"], credential["api_secret"])
        auth.set_access_token(credential["access_token"], credential["access_token_secret"])
        return tweepy.API(auth, wait_on_rate_limit=True)

    # def db(self):
    #     credential = self.load_config()
    #     username = credential["db_username"]
    #     password = credential["db_password"]
    #     host = credential["db_host"]
    #     port = credential["db_port"]
    #     db_name = credential["db_name"]

    #     server = couchdb.Server(f"http://{username}:{password}@{host}:{port}")
    #     return server[db_name]
    