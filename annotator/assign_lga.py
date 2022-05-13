import time
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


from db_utils import DbUtils
from utils import load_polygons, assign_lga_to_tweet


def append_lga_to_tweets(polygons, db):
    """Assign LGA to tweet.

    Args:
        polygons (_type_): _description_
    """
    batch_size = 5
    query = {
        "selector": {
            "geo": {
                "$ne": None
            },
            "extra.lga": {
                "$exists": False
            },
            "extra.lga_unknown": {
                "$exists": False
            },
        },
        "limit": batch_size,
        "skip": 0,
    }

    for doc in db.find(query):
        print(">>> Tweets found")
        try:
            doc = assign_lga_to_tweet(polygons, doc)
            db.save(doc)
        except Exception as e:
            print(f">>> Failed to save: {e}")



if __name__ == "__main__":
    """Continuously look for tweets that have not been annotated."""

    db = DbUtils.connect("twitter_historical")
    wait_till_next_run = 60
    polys = load_polygons()
    while True:
        try:
            print(">>> Looking for tweets")
            append_lga_to_tweets(polys, db)
        except Exception as e:
            print(f">>> ERROR occurred: {e}")

        print(f">>> Sleep for {wait_till_next_run} seconds")
        time.sleep(wait_till_next_run)
