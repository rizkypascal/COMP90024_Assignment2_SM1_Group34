"""
    TODO:
        - error handling duplicate entry on tweet
        - error handling when reach limit
        - filtering with location, maxId / sinceId
"""
class Search:
    def __init__(self, api, db, query):
        self.api = api
        self.db = db
        self.query = query
    
    def save(self, tweet):
        self.db.save(tweet._json)
    
    def search(self):
        for tweet in self.api.search_tweets(q=self.query, count=1):
            self.save(tweet)



