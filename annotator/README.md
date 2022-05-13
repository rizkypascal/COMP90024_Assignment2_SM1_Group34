# Tweet LGA Annotator

This is a python application that search for Tweets in existing database
and based on its geo location information, it will annotate which Local Government Area (LGA) the tweet was tweeted from.

It will search for existing Tweets in `twitter_historical` database that satisfies the following criteria:
* Has `geo` location field
* Has not been annotated before with Local Government Area (LGA) information

Then, it will read from `lga` database that contains data of Local Government Area in Victoria including their geo coordinates.

Using this information, this application will identify from which LGA a Tweet was tweeted from.

To run this application, you will need to create a `config.json` file with the following content:
```
{
    "db_username": <COUCHDB USERNAME>,
    "db_password": <COUCHDB PASSWORD>,
    "db_host": <COUCHDB SERVER IP ADDRESS>,
    "db_port": <COUCHDB PORT>,
    "db_name": <DEFAULT DATABASE TO CONNECT TO>
}
```

## To run without Docker
Create virtual environment and install:
```
python3 -m venv venv
pip install -r requirements.txt
```

Run:
```
source venv/bin/activate
python -u assign_lga.py
```

## To run with Docker

To build or rebuild
```
docker-compose build --no-cache
```

Spin up container:
```
docker-compose up -d
```
