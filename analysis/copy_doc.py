from db_utils import DbUtils


def copy_docs(src_db, dest_db, query, batch_size):
    """Copy document from one database to another.

    Args:
        src_db (_type_): source database
        dest_db (_type_): destination database
        query (_type_): query to filter the source documents
        batch_size (_type_): query batch size
    """
    reach_last_doc = False
    batch = 1
    while not reach_last_doc:
        doc_count = 0
        for doc in src_db.find(query):
            try:
                doc_count += 1
                print(doc["_id"])
                del(doc["_rev"])
                
                dest_db.save(doc)
                
            except Exception as e:
                print(f"Failed to save: {e}")

        batch += 1
        query["skip"] = int(batch * batch_size)

        if doc_count < batch_size:
            reach_last_doc = True

        print("batch", batch)

if __name__ == "__main__":
    """Copy documents from harvested twitter database to the historical twitter database.
    """
    src_db = DbUtils.connect("twitter")
    dest_db = DbUtils.connect("twitter_historical")
    batch_size = 100

    query = {
        "selector": {
            "geo": {
                "$ne": None
            },
            "copied": {
                "$exists": False
            },
        },
        "limit": batch_size,
        "skip": 0,
    }

    copy_docs(src_db, dest_db, query, batch_size)
