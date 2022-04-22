from stream import Stream
from search import Search
import tweepy
import couchdb

API_KEY = "j95ClC3IehZBDJQNMRTW9gQGl"
API_SECRET = "uymxiL0nOkD5kNTT5PRCYNyj0eWIprpEYoG73nNTJ8KHDydCnF"
ACCESS_TOKEN = "1496071983326703617-uUvH0f50872h4djpu7KAF2HXzxra1Y"
ACCESS_TOKEN_SECRET = "82GngChsZKfYwFkNa8aqaMI4qv6KJoA0nq76Px2aKejac"

#couchdb.http.Unauthorized

if __name__ == "__main__":
    # try:
    server = couchdb.Server("http://user:pass@127.0.0.1:15984")
    db = server["testing"]

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    search = Search(api, db, "test")
    search.search()

    stream = Stream(API_KEY, API_SECRET,ACCESS_TOKEN ,ACCESS_TOKEN_SECRET, db)
    stream.stream()
    # except tweepy.TweepError as e:
    #     print("Twitter client auth error: {}".format(e))
    #     return None