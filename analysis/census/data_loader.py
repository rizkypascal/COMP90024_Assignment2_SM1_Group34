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
import argparse
import os
sys.path.append("..")

from db_utils import DbUtils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", help="DB name for census year (example: census_<year>", required=True)
    parser.add_argument("--file", help="File path to the census json file", dest="census_file_path", required=True)
    parser.add_argument("--type", help="Census data type identifier", dest="census_data_type", required=True)
    parser.add_argument("--code", help="Census data code identifier", dest="census_data_code", required=True)
    parser.add_argument("--year", help="Census year", dest="census_year", default=2016, required=False)

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
                doc["source"] = {
                    "name": args.census_data_type,
                    "census_code": args.census_data_code,
                    "census_year": args.census_year
                }
                db.save(doc)
    except Exception as e:
        print(f"ERROR (Census): Exception caught when processing file: {e}")
        exit()
