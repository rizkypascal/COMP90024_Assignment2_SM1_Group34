from flask import Flask, request
from flask_cors import CORS
from datetime import date
from db_utils import DbUtils

import json
import couchdb

app = Flask(__name__)

LGA_DB = DbUtils.connect(db_name="lga")

CORS = CORS()


def get_tweet_count(input):
    return input.get("tweet_count")


@ app.route("/api/test", methods=["GET"])
def test():
    return {"data": ["test1", "test2", "test3"]}


@ app.route("/api/lgas", methods=["GET"])
def info():
    # Read params
    params = request.args
    compact = params.get("compact", False)
    if compact in ("true", "True", 1):
        compact = True

    if compact:
        res1 = []
        res2 = []
        mango1 = {"selector": {}, "limit": 45}
        for row in LGA_DB.find(mango1):
            res1.append(row["properties"]["lga_name_2016"])
            res2.append(row["properties"]["lga_code_2016"])
        return {"lgaNames": res1, "lgaCodes": res2}
    else:
        res1 = []
        mango1 = {"selector": {}, "limit": 45}
        for row in LGA_DB.find(mango1):
            res1.append(row)
        return {"lgaDetails": res1}


@ app.route("/api/twitter/<period>/lgas/<lga_id>", methods=["GET"])
def twitter_per_lga(lga_id, period):
    """_summary_

    Args:
        lga_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    if period.lower() != "all":
        return "Invalid period: should be one of [all]", 422

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
    total_count = 0

    for row in lga_lang_count:
        if(row["key"][1] == str(lga_id)):
            if row["key"][0] in lang_mapper.keys():
                tweet_languages.append({
                    "code": row["key"][0],
                    "name": lang_mapper[row["key"][0]],
                    "tweet_count": row["value"]
                })
                total_count += row["value"]
    tweet_languages.sort(key=get_tweet_count, reverse=True)

    for row in tweet_languages:
        row["tweet_count"] = row["tweet_count"]/total_count

    return {
        "data": {
            "code": properties["lga_code_2016"],
            "name": properties["lga_name_2016"],
            "tweet_languages": tweet_languages
        }, "total_count": total_count
    }


@ app.route("/api/twitter/<period>/lgas", methods=["GET"])
def twitter_lgas(period):
    """summary of twitter data per lgas

    Args:
        lga_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    if period.lower() != "all":
        return "Invalid period: should be one of [all]", 422

    with open("language.json", "r") as f:
        lang_mapper = json.load(f)

    lga_unique_lang = DbUtils.view(
        db="twitter_historical",
        design="matilda_test",
        view="list_all_langs_in_lga",
        group_level=1
    )

    if(lga_unique_lang is None):
        return {"data": {}}

    lgas = []
    for row in lga_unique_lang:
        lga_code = row["key"][0]
        lang_codes = row["value"]

        tweet_unique_languages = []
        for lang_code in lang_codes:
            lang_name = lang_mapper.get(lang_code, "")
            tweet_unique_languages.append({
                "code": lang_code,
                "name": lang_name
            })

        lgas.append({
            "lga_code_2016": lga_code,
            "tweet_languages": tweet_unique_languages
        })

    return {
        "data": lgas
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
