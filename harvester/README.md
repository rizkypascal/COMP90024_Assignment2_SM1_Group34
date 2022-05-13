# Tweet Harverster

This is a python application that uses Twitter API to search for recent Tweets whose user profile stated that they are in Melbourne and its surrouding area.

To run this application, you will need to create a `config.json` file with the following content:
```
{
    "api_key": <TWITTER API KEY>,
    "api_secret": <TWITTER API SECRET>,
    "access_token": <TWITTER API ACCESS TOKEN>,
    "access_token_secret": <TWITTER API ACCESS TOKEN SECRET>,
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
python -u stream.py
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
