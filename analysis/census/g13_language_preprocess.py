import sys
import os
import pandas as pd
import census_utils


def main():
    
    # G13 tables from 2016 Census contain data for 'Language spoken at home'
    # LGA-level G13c and G13d datasets were obtained from AURIN
    ROOT_PATH = './'
    DATA_DIR = 'aurin_data'
    MAPPING_DIR = 'mapping'
    G13c_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g13c_lang_spoken_at_home_by_profic_by_sex_census_2016-5202467057275348071.json')
    G13d_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g13d_lang_spoken_at_home_by_profic_by_sex_census_2016-8416648648204931958.json')
    MAPPING_PATH = os.path.join(ROOT_PATH, MAPPING_DIR, 'g13_language_mapping.json')  # this mapping was preprocessed from AURIN metadata for G13
    OUTPUT_JSON_PATH = os.path.join(ROOT_PATH, 'census_LGA-G13_proportions.json')

    # read jsons into dataframes
    df_G13c = census_utils.read_census_json(G13c_PATH)
    df_G13d = census_utils.read_census_json(G13d_PATH)
    
    # combines dataframes, preprocess columns, and unpivot
    df_G13 = process_G13_df(df_G13c, df_G13d)
    
    # calculates proportions and map variable names into attribute names
    df_LGA_proportions = census_utils.calc_LGA_proportions(df_G13)
    df_LGA_proportions = census_utils.map_variable_names(df_LGA_proportions, MAPPING_PATH)
    df_LGA_proportions.to_json(OUTPUT_JSON_PATH, orient='table', index=False)
    
    return 0


def process_G13_df(df_G13c, df_G13d):
    '''
    Takes in raw G13c and G13d dataframes, and performs the following
    - Combines G13c and G13d into a single df
    - Drops columns that would've caused double-counting, and select only relevant columns
    - Unpivots df to make it easier for subsequent processing
    '''
    
    # combine G13c and G13d
    df = df_G13c.join(df_G13d)

    # drop and/or select only columns that we need
    df = df.loc[:, ~df.columns.str.startswith('female_')]  # drop columns that start with 'female_'
    df = df.loc[:, ~df.columns.str.startswith('person_tot_')]  # drop columns that start with 'person_tot_'
    df = df.loc[:, ~df.columns.str.startswith('person_spks_lang_oth_')]  # drop columns that start with 'person_spks_lang_oth_'
    df = df.loc[:, ~df.columns.str.endswith('_tot_tot')]  # drop columns that contain '_tot_tot'
    df = df.loc[:, df.columns.str.endswith('_tot')]  # only take columns that end with '_tot'

    # unpivot df
    df_unpivot = pd.melt(df.reset_index(), id_vars=df.index.names)

    return df_unpivot


if __name__ == '__main__':
    sys.exit(main())
    
