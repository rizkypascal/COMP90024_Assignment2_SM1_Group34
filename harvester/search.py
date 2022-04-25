from twitter_utils import TwitterUtils
import tweepy
import couchdb
import logging
import logger

"""
    TODO:
        - error handling duplicate entry on tweet
        - error handling when reach limit
        - filtering with location, maxId / sinceId
"""

tweets_count = 0 # to count how many tweets have been saved

class Search:
    def __init__(self, api, db, query):
        self.api = api
        self.db = db
        self.query = query
        self.tweets_count = tweets_count
    
    def save(self, tweet):
        self.db.save(tweet._json)
    
    def search(self):
        try:
            for tweet in self.api.search_tweets(q=self.query, count=1):
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
    twitter_utils = TwitterUtils()
    api = twitter_utils.client()
    db = twitter_utils.db()
    
    while True:
        logging.info("harvesting search starting")
        search = Search(api, db, "test")
        search.search()
