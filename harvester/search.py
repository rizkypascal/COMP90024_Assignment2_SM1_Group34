"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

from twitter_utils import TwitterUtils
from db_utils import DbUtils
import tweepy
import couchdb
import logging
import logger

tweets_count = 0 # to count how many tweets have been saved

class Search:
    def __init__(self, api, db, query):
        self.api = api
        self.db = db
        self.query = query
        self.tweets_count = tweets_count
    
    def save(self, tweet):
        doc = tweet._json

        # create partition id
        tweet_id = doc["id"]
        lang = doc["lang"]
        doc_id = f"{lang}:{tweet_id}"
        doc["_id"] = doc_id

        self.db.save(doc)
    
    def search(self):
        try:
            for tweet in self.api.search_tweets(q=self.query, count=1, include_entities=False):
                try:
                    self.save(tweet)
                    self.tweets_count += self.tweets_count + 1
                except (couchdb.http.Unauthorized, couchdb.http.ResourceNotFound) as e:
                    logging.error("Couch db resource error: {}".format(str(e)))
                    break
                except (BaseException) as e:
                    logging.warning("Couch db save: {}".format(str(e)))
                    continue
        except tweepy.errors.TweepyException as e:
            logging.error("Twitter search error: {}".format(str(e)))

if __name__ == "__main__":
    logging.basicConfig(level=logging.CRITICAL)
    twitter_utils = TwitterUtils()
    db_utils = DbUtils()

    api = twitter_utils.client()
    db = db_utils.connect()
    
    count = 1
    while count > 0:
        logging.info("harvesting search starting")
        search = Search(api, db, "test")
        search.search()

        count -= 1
