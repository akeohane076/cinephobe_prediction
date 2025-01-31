import pandas as pd

from data.constants import CATEGORY_MAPPING

def extract_num_reviews(x):
    s = str(x).replace('+', '').replace('<', '').replace('V', '').strip()
    if s == "nan":
        return 'nan'
    if 'k' or 'K' in s:
        return float(s.replace('k','').replace('K', '')) * 1000
    else:
        print(s)
        return int(s)
    

def extract_mil_value(x):
    # Check if the value is a valid float or can be converted to a float
    s = str(x)
    if not any(char.isnumeric() for char in s):
        return 'nan'
    if '-' in x:
        return 'nan'
    if '?' in x:
        return 'nan'
    if '/' in x:
        return 'nan'
    if ',' in x:
        return 'nan'
    if ' ' not in x:
        return 'nan'
    v = s.replace('$', '').replace(' Mil', '').replace('+', '')
    return float(v) * 1000000


def map_cost_values(x):
    if x == '$':
        return 1
    else:
        return 0

def map_pick_values(x):
    if x == 'A':
        return 0
    elif x == 'Z':
        return 1
    elif x == 'M':
        return 2
    else:
        return 3

def map_percents(x):
    s = str(x)
    if '--' in s:
        return 'nan'
    if '%' in s:
        return int(s.replace('%', '').replace('.00',''))
    if isinstance(x, str):
        return x

def categorize_genres_for_row(g):
    """
    Categorize a genre string into binary categories based on predefined keywords.
    Each category gets a 1 if the genre matches, 0 otherwise.
    """
    # Split the genre string into a list (if it's a comma-separated string)
    row_genres = g.lower()
    
    # Prepare a binary dictionary for each category
    category_results = {category: 0 for category in CATEGORY_MAPPING}
    
    # Check each category for keywords in the genres
    for category, keywords in CATEGORY_MAPPING.items():
        if any(keyword in row_genres for keyword in keywords):
            category_results[category] = 1
    
    return category_results

def add_category_columns(df, genre_column):
    """
    Add binary category columns to the DataFrame based on the genre column.
    """
    # Apply the categorization function to each row in the genre column
    categories = df[genre_column].apply(lambda x: categorize_genres_for_row(x))

    # Convert the results into separate columns
    category_df = pd.DataFrame(categories.tolist(), columns=CATEGORY_MAPPING.keys())
    
    # Concatenate the original dataframe with the new category columns
    df = pd.concat([df, category_df], axis=1)
    
    return df