"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)