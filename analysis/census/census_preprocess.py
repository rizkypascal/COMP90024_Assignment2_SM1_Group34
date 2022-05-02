import sys
import json
import pandas as pd


def main():
    
    # G13 tables from 2016 Census contain data for 'Language spoken at home'
    # LGA-level G13c and G13d datasets were obtained from AURIN
    DATA_PATH = './'
    G13c_PATH = DATA_PATH + 'lga_G13c_lang_spoken_at_home_by_profic_by_sex_census_2016-5202467057275348071.json'
    G13d_PATH = DATA_PATH + 'lga_G13d_lang_spoken_at_home_by_profic_by_sex_census_2016-8416648648204931958.json'
    LANGUAGE_MAPPING_PATH = DATA_PATH + 'language_mapping.json'  # this mapping was preprocessed from AURIN metadata for G13

    # read jsons into dataframes
    df_G13c = read_G13(G13c_PATH)
    df_G13d = read_G13(G13d_PATH)
    
    # combines G13c and G13d, preprocess columns, and unpivot
    df_G13 = process_G13_dfs(df_G13c, df_G13d)
    df_G13.to_json('census_LGA-G13.json', orient='table', index=False)
    
    # calculates proportions and map variable names into language names
    df_LGA_proportions = calc_LGA_proportions(df_G13)
    df_LGA_proportions = map_language_names(df_LGA_proportions, LANGUAGE_MAPPING_PATH)
    df_LGA_proportions.to_json('census_LGA-G13_proportions.json', orient='table', index=False)
    
    return 0


def read_G13(path):
    '''
    Reads G13c/G13d json into a dataframe
    '''

    with open(path) as f:
        data = json.load(f)
    f.close()
    
    df = pd.DataFrame([d['properties'] for d in data['features']]).set_index(['lga_code_2016','lga_name_2016'])
    return df


def process_G13_dfs(df_G13c, df_G13d):
    '''
    Takes in raw G13c and G13d dataframes, and performs the following
    - Combines G13c and G13d into a single df
    - Drops columns that would've caused double-counting, and select only relevant columns
    - Unpivots df to make it easier for subsequent processing
    '''
    
    # combine G13c and G13d
    df_G13 = df_G13c.join(df_G13d)

    # drop and/or select only columns that we need
    df_G13 = df_G13.loc[:, ~df_G13.columns.str.startswith('female_')]  # drop columns that start with 'female_'
    df_G13 = df_G13.loc[:, ~df_G13.columns.str.startswith('person_tot_')]  # drop columns that start with 'person_tot_'
    df_G13 = df_G13.loc[:, ~df_G13.columns.str.startswith('person_spks_lang_oth_')]  # drop columns that start with 'person_spks_lang_oth_'
    df_G13 = df_G13.loc[:, ~df_G13.columns.str.endswith('_tot_tot')]  # drop columns that contain '_tot_tot'
    df_G13 = df_G13.loc[:, df_G13.columns.str.endswith('_tot')]  # only take columns that end with '_tot'

    # unpivot df
    df_G13_unpivot = pd.melt(df_G13.reset_index(), id_vars=df_G13.index.names)

    return df_G13_unpivot


def calc_LGA_proportions(df_G13):
    '''
    Calculates langugage proportions for each LGA
    '''
    
    # calculate total population for each LGA
    df_LGA_totals = df_G13.groupby(['lga_code_2016','lga_name_2016'], as_index=False).sum().rename(columns={'value':'total'})

    # calculate proportion for each language
    df_LGA_proportions = pd.merge(df_G13, 
                                  df_LGA_totals, 
                                  left_on=['lga_code_2016','lga_name_2016'], 
                                  right_on=['lga_code_2016','lga_name_2016'])
    df_LGA_proportions['proportion'] = df_LGA_proportions['value'] / df_LGA_proportions['total']
    
    return df_LGA_proportions


def map_language_names(df_LGA_proportions, language_mapping_path):
    '''
    Maps G13 variable names (eg. 'person_spks_french_tot') to language names (eg. 'French')
    '''
    
    language_mapping = pd.read_json(language_mapping_path, orient='table')
    df_LGA_proportions = pd.merge(df_LGA_proportions, 
                                  language_mapping, 
                                  left_on='variable', 
                                  right_on='variable')
    
    return df_LGA_proportions


if __name__ == '__main__':
    sys.exit(main())
    
