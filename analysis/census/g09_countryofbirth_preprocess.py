"""
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
"""

import sys
import os
import pandas as pd
import census_utils


def main():
    
    # G09 tables from 2016 Census contain data for 'Country of birth'
    # LGA-level G09f, G09g, and G09h datasets were obtained from AURIN
    ROOT_PATH = './'
    DATA_DIR = 'aurin_data'
    MAPPING_DIR = 'mapping'
    G09f_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g09f_country_of_birth_by_age_by_sex_census_2016-6975652387153791005.json')
    G09g_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g09g_country_of_birth_by_age_by_sex_census_2016-3857234076788626972.json')
    G09h_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g09h_country_of_birth_by_age_by_sex_census_2016-4328583804824129071.json')
    MAPPING_PATH = os.path.join(ROOT_PATH, MAPPING_DIR, 'g09_countryofbirth_mapping.json')  # this mapping was preprocessed from AURIN metadata for G09
    OUTPUT_JSON_PATH = os.path.join(ROOT_PATH, 'census_LGA-G09_proportions.json')

    # read jsons into dataframes
    df_G09f = census_utils.read_census_json(G09f_PATH)
    df_G09g = census_utils.read_census_json(G09g_PATH)
    df_G09h = census_utils.read_census_json(G09h_PATH)
    
    # combines dataframes, preprocess columns, and unpivot
    df_G09 = process_G09_df(df_G09f, df_G09g, df_G09h)
    
    # calculates proportions and map variable names into attribute names
    df_LGA_proportions = census_utils.calc_LGA_proportions(df_G09)
    df_LGA_proportions = census_utils.map_variable_names(df_LGA_proportions, MAPPING_PATH)
    df_LGA_proportions.to_json(OUTPUT_JSON_PATH, orient='table', index=False)
    
    return 0


def process_G09_df(df_G09f, df_G09g, df_G09h):
    '''
    Takes in raw G09 dataframes, and performs the following
    - Combines G09f, G09g, and G09h into a single df
    - Drops columns that would've caused double-counting, and select only relevant columns
    - Unpivots df to make it easier for subsequent processing
    '''
    
    # combine G09f, G09g, and G09h
    df = df_G09f.join(df_G09g).join(df_G09h)

    # drop and/or select only columns that we need
    df = df.loc[:, ~df.columns.str.startswith('f_')]  # drop columns that start with 'f_'
    df = df.loc[:, ~df.columns.str.startswith('p_tot')]  # drop columns that start with 'p_tot'
    df = df.loc[:, df.columns.str.endswith('_tot')]  # only take columns that end with '_tot'

    # unpivot df
    df_unpivot = pd.melt(df.reset_index(), id_vars=df.index.names)

    return df_unpivot


if __name__ == '__main__':
    sys.exit(main())
    
