"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

import g08_ancestry_preprocess
import g09_countryofbirth_preprocess
import g13_language_preprocess
import g14_religion_preprocess

if __name__ == '__main__':
    g08_ancestry_preprocess.main()
    g09_countryofbirth_preprocess.main()
    g13_language_preprocess.main()
    g14_religion_preprocess.main()