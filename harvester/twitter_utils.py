"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

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
    