import json
import pandas as pd

def read_census_json(path):
    '''
    Reads census json into a dataframe
    '''

    with open(path) as f:
        data = json.load(f)
    f.close()
    
    df = pd.DataFrame([d['properties'] for d in data['features']]).set_index(['lga_code_2016','lga_name_2016'])
    return df


def calc_LGA_proportions(df):
    '''
    Calculates attribute proportions for each LGA
    '''
    
    # calculate total population for each LGA
    df_LGA_totals = df.groupby(['lga_code_2016','lga_name_2016'], as_index=False).sum().rename(columns={'value':'total'})

    # calculate proportion for each attribute
    df_LGA_proportions = pd.merge(df, 
                                  df_LGA_totals, 
                                  left_on=['lga_code_2016','lga_name_2016'], 
                                  right_on=['lga_code_2016','lga_name_2016'])
    df_LGA_proportions['proportion'] = df_LGA_proportions['value'] / df_LGA_proportions['total']
    
    return df_LGA_proportions


def map_variable_names(df_LGA_proportions, path):
    '''
    Maps Census variable names (eg. 'person_spks_french_tot') to attribute names (eg. 'French')
    '''
    
    mapping = pd.read_json(path, orient='table')
    df_LGA_proportions = pd.merge(df_LGA_proportions, 
                                  mapping, 
                                  left_on='variable', 
                                  right_on='variable')
    
    return df_LGA_proportions