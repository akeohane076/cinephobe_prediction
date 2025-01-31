import re
import pandas as pd
import numpy as np

from data.grooming_functions import extract_num_reviews, extract_mil_value, map_cost_values, map_pick_values, map_percents, add_category_columns
from data.constants import keep, pick_value_map, rows_to_drop, cols_to_drop, float_cols

def load_data(file_path):
    return pd.read_csv(file_path)

def groom_data(df_raw):
    df = df_raw[keep]
    df = df[~df['Movie'].isin(rows_to_drop) & df['Movie'].notna()]

    df['Cost'] = df['Cost'].apply(map_cost_values)

    # this will convert the string of who picked the movie, to a numerical catgorical feature
    df['Pick'] = df['Pick'].apply(map_pick_values)

    df_encoded = pd.get_dummies(df['Pick'], prefix="Pick", drop_first=False)
    df_encoded = df_encoded.astype(int)

    df = pd.concat([df, df_encoded], axis=1)

    # these groom the dollar amounts and turn them into float values
    df['Budget'] = df['Budget'].apply(extract_mil_value)
    df['Box Off WW'] = df['Box Off WW'].apply(extract_mil_value)


    df['RT Crit'] = df["RT Crit"].apply(map_percents)
    df['RT Aud'] = df["RT Aud"].apply(map_percents)

    df['Combo'] = df["Combo"].apply(map_percents)

    df['Aud #'] = df['Aud #'].apply(extract_num_reviews)

    max_value = df['Aud #'].max()

    # Step 2: Replace the largest value with NaN
    df['Aud #'] = df['Aud #'].replace(max_value, np.nan)

    # remove unnamed rows from csv. 
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df = add_category_columns(df, 'Genre')

    df = df.drop(columns=cols_to_drop)
    df = df.iloc[:-6]
    for col in float_cols:
        df[col] = df[col].apply(lambda x: x if isinstance(x, float or int) else 0)
    df_clean = df.dropna()
    

    return df_clean