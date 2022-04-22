import tweepy

"""
    TODO:
        - error handling duplicate entry on tweet
        - error handling others
        - filtering with location
        - define bounding box melbourne
"""
class StreamListener(tweepy.Stream):
    def __init__(self, *args, **kwargs):
        super(StreamListener, self).__init__(*args)
        self.db = kwargs["db"]
    def on_error(self, status_code):
        print(status_code)
        if status_code == '420':
            return False
    def on_status(self, status):
        self.db.save(status._json)

class Stream:
    def __init__(self, apiKey, apiSecret, accessToken, accessTokenSecret, db):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.accessToken = accessToken
        self.accessTokenSecret = accessTokenSecret
        self.db = db
    def stream(self):
        stream = StreamListener(self.apiKey, self.apiSecret, self.accessToken, self.accessTokenSecret, db = self.db)
        stream.filter(track=["Melbourne"])#,locations=[144.931641,-37.814124,144.931641,-37.814124])