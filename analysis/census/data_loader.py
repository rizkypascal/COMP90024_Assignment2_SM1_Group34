import json
import sys
import argparse
import os
sys.path.append("..")

from db_utils import DbUtils


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", help="DB name for census year (example: census_<year>", required=True)
    parser.add_argument("--census", help="File path to the census json file", dest="census_file_path", required=True)

    args = parser.parse_args()
    census_file_path = os.path.abspath(args.census_file_path)

    # dynamic db name to handle more census years
    db = DbUtils.connect(db_name=args.db)

    if not os.path.exists(census_file_path):
        print(f"ERROR (Census): Census file {census_file_path} does not exist.")
        exit()

    try:
        with open(census_file_path, "r") as f:
            rows = json.load(f).get("data")

            for doc in rows:
                id = f"{doc['lga_code_2016']}:{doc['variable']}"
                doc["_id"] = id
                db.save(doc)
    except Exception as e:
        print(f"ERROR (Census): Exception caught when processing file: {e}")
        exit()
