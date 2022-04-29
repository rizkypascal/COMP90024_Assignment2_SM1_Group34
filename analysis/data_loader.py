import json
import sys
from db_utils import DbUtils


if __name__ == "__main__":
    db = DbUtils.connect(db_name="juny-test")


    if len(sys.argv) <= 1:
        print("ERROR: Please provide json file")
        exit()

    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        data = json.load(f)

        rows = data.get("features")

        for doc in rows:
            props = doc.get("properties", {})

            id = f"{props['state_code_2016']}:{props['lga_code_2016']}"

            # EDIT: must provide document id
            doc["_id"] = id
            db.save(doc)
