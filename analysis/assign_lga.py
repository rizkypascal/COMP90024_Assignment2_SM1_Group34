import time
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
    batch_size = 100
    query = {
        "selector": {
            "geo": {
                "$ne": None
            },
            "extra.lga": {
                "$exists": False
            },
            "lga_unknown": {
                "$exists": False
            },
        },
        "limit": batch_size,
        "skip": 0,
    }

    reach_last_doc = False
    batch = 1
    while not reach_last_doc:
        print("batch", batch)

        doc_count = 0
        for doc in db.find(query):
            try:
                doc_count += 1
                doc = assign_lga_to_tweet(polygons, doc)
                db.save(doc)
            except Exception as e:
                print(f"Failed to save: {e}")

        batch += 1
        query["skip"] = int(batch * batch_size)

        if doc_count < batch_size:
            reach_last_doc = True



if __name__ == "__main__":
    db = DbUtils.connect("twitter_historical")
    wait_till_next_run = 60
    polys = load_polygons()
    while True:
        append_lga_to_tweets(polys, db)

        print(f"Sleep for {wait_till_next_run} seconds")
        time.sleep(wait_till_next_run)
