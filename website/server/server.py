from flask import Flask
from flask_cors import CORS

from db_utils import DbUtils
import json

app = Flask(__name__)

LGA_DB = DbUtils.connect(db_name="lga")

CORS = CORS()


@ app.route("/api/test", methods=["GET"])
def test():
    return {"data": ["test1", "test2", "test3"]}


@ app.route("/api/lgas", methods=["GET"])
def info():
    res = []
    mango1 = {"selector": {}, "limit": 45}
    for row in LGA_DB.find(mango1):
        res.append(row["properties"]["lga_name_2016"])
    return {"data": res}

@ app.route("/api/lgas/<lga_id>")
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
        db="twitter",
        design="lga_count",
        view="lga-language-count",
        group_level=2
    )

    if(lga_lang_count is None):
        return {"data": {}}

    tweet_languages = []

    for row in lga_lang_count:
        if(row["key"][0] == str(lga_id)):
            tweet_languages.append({
                "code": row["key"][1],
                "name": lang_mapper[row["key"][1]],
                "tweet_count": row["value"]
            })

    return {
        "data": {
            "code": properties["lga_code_2016"],
            "name": properties["lga_name_2016"],
            "tweet_languages": tweet_languages
        }
    }

if __name__ == "__main__":
    app.run(debug=True)

# Test route


print('hello')
print(info())
