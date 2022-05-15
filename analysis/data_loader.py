"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

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
