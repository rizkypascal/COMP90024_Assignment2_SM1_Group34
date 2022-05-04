import sys
import os
import pandas as pd
import census_utils


def main():
    
    # G08 tables from 2016 Census contain data for 'Ancestry'
    # LGA-level G08 datasets were obtained from AURIN
    ROOT_PATH = './'
    DATA_DIR = 'aurin_data'
    MAPPING_DIR = 'mapping'
    G08_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g08_ancestry_parents_country_of_birth_census_2016-8078327263249365634.json')
    MAPPING_PATH = os.path.join(ROOT_PATH, MAPPING_DIR, 'g08_ancestry_mapping.json')  # this mapping was preprocessed from AURIN metadata for G08
    OUTPUT_JSON_PATH = os.path.join(ROOT_PATH, 'census_LGA-G08_proportions.json')

    df_G08 = census_utils.read_census_json(G08_PATH)
    
    # preprocess columns, and unpivot
    df_G08 = process_G08_df(df_G08)
    
    # calculates proportions and map variable names into attribute names
    df_LGA_proportions = census_utils.calc_LGA_proportions(df_G08)
    df_LGA_proportions = census_utils.map_variable_names(df_LGA_proportions, MAPPING_PATH)
    df_LGA_proportions.to_json(OUTPUT_JSON_PATH, orient='table', index=False)
    
    return 0


def process_G08_df(df):
    '''
    Takes in raw G08 dataframe, and performs the following
    - Drops columns that would've caused double-counting, and select only relevant columns
    - Unpivots df to make it easier for subsequent processing
    '''

    # drop and/or select only columns that we need
    df = df.loc[:, df.columns.str.endswith('_tot_responses')]  # only take columns that end with '_tot_responses'
    df = df.loc[:, ~df.columns.str.startswith('tot_p_')]  # drop columns that start with 'tot_p_'

    # unpivot df
    df_unpivot = pd.melt(df.reset_index(), id_vars=df.index.names)

    return df_unpivot


if __name__ == '__main__':
    sys.exit(main())
    
