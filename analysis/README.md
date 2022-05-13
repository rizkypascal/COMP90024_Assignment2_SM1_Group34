# Analysis

This folder contains the python scripts:
* `census` folder: scripts to preprocess AURIN data
* `data_loader.ph`: python script to load historic Twiter data into the CouchDB database
* `copy_doc.py`: Early in the implementation, we store recent Tweets we harvested into a database called `twitter`. We then copy these Tweets into the main database that contains most of the historic tweets in `twitter_historical` database.