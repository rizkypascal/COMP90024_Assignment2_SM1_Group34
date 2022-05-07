from flask import Flask
from flask_cors import CORS
from datetime import date
from db_utils import DbUtils

import json
import couchdb

app = Flask(__name__)

LGA_DB = DbUtils.connect(db_name="lga")

CORS = CORS()


@ app.route("/api/test", methods=["GET"])
def test():
    return {"data": ["test1", "test2", "test3"]}


@ app.route("/api/lga_details/lga_names", methods=["GET"])
def info():
    res1 = []
    res2 = []
    mango1 = {"selector": {}, "limit": 45}
    for row in LGA_DB.find(mango1):
        res1.append(row["properties"]["lga_name_2016"])
        res2.append(row["properties"]["lga_code_2016"])
    return {"lgaNames": res1, "lgaCodes": res2}


@ app.route("/api/lga_details", methods=["GET"])
def lgadetails():
    res1 = []
    mango1 = {"selector": {}, "limit": 45}
    for row in LGA_DB.find(mango1):
        res1.append(row)
    return {"lgaDetails": res1}


@ app.route("/api/lgas/<lga_id>", methods=["GET"])
def lgas(lga_id):

    with open("language.json", "r") as f:
        lang_mapper = json.load(f)

    mango = {
        "selector": {
            "_id": f"2:{lga_id}"
        },
        "fields": ["properties"]
    }

    properties = {}

    for row in LGA_DB.find(mango):
        properties = row["properties"]

    lga_lang_count = DbUtils.view(
        db="twitter_historical",
        design="lga_count",
        view="lga-language-count",
        group_level=2
    )

    if(lga_lang_count is None):
        return {"data": {}}

    tweet_languages = []

    for row in lga_lang_count:
        if(row["key"][1] == str(lga_id)):
            if row["key"][0] in lang_mapper.keys():
                tweet_languages.append({
                    "code": row["key"][0],
                    "name": lang_mapper[row["key"][0]],
                    "tweet_count": row["value"]
                })

    return {
        "data": {
            "code": properties["lga_code_2016"],
            "name": properties["lga_name_2016"],
            "tweet_languages": tweet_languages
        }
    }


@ app.route("/api/census/<census_year>/lgas/<lga_id>/<category>", methods=["GET"])
def census_lga(census_year, lga_id, category):

    try:
        census_year = int(census_year)
    except ValueError:
        return "Invalid year: should be numeric", 422

    current_year = date.today().year

    if(census_year < 1900 or census_year > current_year):
        return f"Invalid year: range should between 1900 and {current_year}", 422

    try:
        db_name = "census"

        census_db = DbUtils.connect(db_name=db_name)

        mango = {
            "selector": {
                f"lga_code_{census_year}": f"{lga_id}",
                f"source.name": f"{category}",
                f"source.census_year": census_year
            },
            "fields": [
                f"lga_code_{census_year}",
                f"lga_name_{census_year}",
                "variable",
                "value",
                "total",
                "proportion",
                f"{category}"
            ],
            "sort": [{"proportion": "desc"}],
            "limit": 10,
        }

        objects = []

        for row in census_db.find(mango):
            objects.append(row)

        return {"data": objects}
    except (couchdb.http.Unauthorized, couchdb.http.ResourceNotFound) as e:
        return "Data not found", 404


if __name__ == "__main__":
    app.run(debug=True)

# Test route


print('hello')
print(info())
