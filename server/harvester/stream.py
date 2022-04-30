from twitter_utils import TwitterUtils
import tweepy
import couchdb
import logging
import logger

"""
    TODO:
        - error handling duplicate entry on tweet
        - error handling others
        - filtering with location
        - define bounding box melbourne
"""

API_KEY = "j95ClC3IehZBDJQNMRTW9gQGl"
API_SECRET = "uymxiL0nOkD5kNTT5PRCYNyj0eWIprpEYoG73nNTJ8KHDydCnF"
ACCESS_TOKEN = "1496071983326703617-uUvH0f50872h4djpu7KAF2HXzxra1Y"
ACCESS_TOKEN_SECRET = "82GngChsZKfYwFkNa8aqaMI4qv6KJoA0nq76Px2aKejac"

class StreamListener(tweepy.Stream):
    def __init__(self, *args, **kwargs):
        super(StreamListener, self).__init__(*args)
        self.db = kwargs["db"]
    def on_error(self, status_code):
        print(status_code)
        if status_code == '420':
            return False
    def on_status(self, status):
        try:
            doc = status._json

            # create partition id
            tweet_id = doc["id"]
            lang = doc["lang"]
            doc_id = f"{lang}:{tweet_id}"
            doc["_id"] = doc_id

            self.db.save(doc)
        except (couchdb.http.Unauthorized, couchdb.http.ResourceNotFound) as e:
            logging.error("Couch db resource error: {}".format(str(e)))
            return False
        except (BaseException) as e:
            logging.warning("Couch db save: {}".format(str(e)))

class Stream:
    def __init__(self, apiKey, apiSecret, accessToken, accessTokenSecret, db):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.accessToken = accessToken
        self.accessTokenSecret = accessTokenSecret
        self.db = db
    def stream(self):
        stream = StreamListener(self.apiKey, self.apiSecret, self.accessToken, self.accessTokenSecret, db = self.db)
        stream.filter(locations=[143.415527,-38.796908,146.260986,-36.553775]) #Melbourne and surrounding (outer area is Maryborough, Bendigo, Seymour, Ballarat, Colac, Rosebud, Warragul)

if __name__ == "__main__":
    twitter_utils = TwitterUtils()
    api = twitter_utils.client()
    db = twitter_utils.db()
    
    while True:
        logging.info("harvesting stream starting")
        stream = Stream(API_KEY, API_SECRET,ACCESS_TOKEN ,ACCESS_TOKEN_SECRET, db)
        stream.stream()
