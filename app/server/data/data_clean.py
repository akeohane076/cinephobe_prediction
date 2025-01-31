import re
import pandas as pd
from grooming_functions import extract_num_reviews, extract_mil_value, map_cost_values, map_pick_values, map_percents, add_category_columns
from constants import keep, pick_value_map, rows_to_drop, cols_to_drop, csv_file_path

# Convert CSV to DataFrame
df_raw = pd.read_csv(csv_file_path)

df = df_raw[keep]
df = df[~df['Movie'].isin(rows_to_drop) & df['Movie'].notna()]

df['Cost'] = df['Cost'].apply(map_cost_values)

# this will convert the string of who picked the movie, to a numerical catgorical feature
df['Pick'] = df['Pick'].apply(map_pick_values)

# these groom the dollar amounts and turn them into float values
df['Budget'] = df['Budget'].apply(extract_mil_value)
df['Box Off WW'] = df['Box Off WW'].apply(extract_mil_value)


df['RT Crit'] = df["RT Crit"].apply(map_percents)
df['RT Aud'] = df["RT Aud"].apply(map_percents)

df['Combo'] = df["Combo"].apply(map_percents)
# df['Sprd'] = df["Sprd"].apply(map_percents)

df['Aud #'] = df['Aud #'].apply(extract_num_reviews)

# remove unnamed rows from csv. 
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df = add_category_columns(df, 'Genre')

df = df.drop(columns=cols_to_drop)

# print(df['Pick'][0:30])

# Display the first few rows of the DataFrame
print(df[150:170])