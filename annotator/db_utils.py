"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

import os
import json
import couchdb


class DbUtils:
    @classmethod
    def load_config(cls):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(curr_dir, "config.json")

        with open(config_file, "r") as f:
            credential = json.load(f)

        return credential

    @classmethod
    def connect(cls, db_name=None):
        credential = cls.load_config()

        username = credential["db_username"]
        password = credential["db_password"]
        host = credential["db_host"]
        port = credential["db_port"]

        if db_name is None:
            db_name = credential["db_name"]

        server = couchdb.Server(f"http://{username}:{password}@{host}:{port}")
        return server[db_name]
