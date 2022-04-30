from flask import Flask
from flask_cors import CORS

import db_utils

app = Flask(__name__)

db = db_utils.DbUtils.connect(db_name="lga")
cors = CORS()


@ app.route("/test", methods=["GET"])
def test():
    return {"data": ["test1", "test2", "test3"]}


@ app.route("/lgas", methods=["GET"])
def info():
    res = []
    mango1 = {"selector": {}, "limit": 45}
    for row in db.find(mango1):
        res.append(row["properties"]["lga_name_2016"])
    return {"data": res}


if __name__ == "__main__":
    app.run(debug=True)

# Test route


print('hello')
print(info())
