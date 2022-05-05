import sys
import os
import pandas as pd
import census_utils


def main():
    
    # G14 tables from 2016 Census contain data for 'Religious Affiliation'
    # LGA-level G14 datasets were obtained from AURIN
    ROOT_PATH = './'
    DATA_DIR = 'aurin_data'
    MAPPING_DIR = 'mapping'
    G14_PATH = os.path.join(ROOT_PATH, DATA_DIR, 'lga_g14_religious_affiliation_by_sex_census_2016-4882852298401738484.json')
    MAPPING_PATH = os.path.join(ROOT_PATH, MAPPING_DIR, 'g14_religion_mapping.json')  # this mapping was preprocessed from AURIN metadata for G14
    OUTPUT_JSON_PATH = os.path.join(ROOT_PATH, 'census_LGA-G14_proportions.json')

    df_G14 = census_utils.read_census_json(G14_PATH)
    
    # preprocess columns, and unpivot
    df_G14 = process_G14_df(df_G14)
    
    # calculates proportions and map variable names into attribute names
    df_LGA_proportions = census_utils.calc_LGA_proportions(df_G14)
    df_LGA_proportions = census_utils.map_variable_names(df_LGA_proportions, MAPPING_PATH)
    df_LGA_proportions.to_json(OUTPUT_JSON_PATH, orient='table', index=False)
    
    return 0


def process_G14_df(df):
    '''
    Takes in raw G14 dataframe, and performs the following
    - Drops columns that would've caused double-counting, and select only relevant columns
    - Unpivots df to make it easier for subsequent processing
    '''

    # drop and/or select only columns that we need
    df = df.loc[:, df.columns.str.endswith('_p')]  # only take columns that end with '_p'
    df = df.loc[:, ~df.columns.str.contains('tot_')]  # drop columns that contain 'tot_'

    # unpivot df
    df_unpivot = pd.melt(df.reset_index(), id_vars=df.index.names)

    return df_unpivot


if __name__ == '__main__':
    sys.exit(main())
    
