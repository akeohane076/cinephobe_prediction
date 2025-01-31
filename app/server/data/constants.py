import numpy as np

keep = ["Zach", "Amin", "Mayes", 'Movie','Year', 'Time', 'Genre', 'Pick', 'RT Crit', 'RT Aud', 'Aud #', 'Combo', 'Budget', 'Box Off WW', 'Cost']

target = ["Zach", "Amin", "Mayes"]

float_cols = ['Year', 'Time', 'Pick', 'RT Aud', 'Aud #', 'Combo', 'Budget', 'Box Off WW', 'Cost', 'Pick_0','Pick_1','Pick_2', 'Pick_3']

cols_to_drop = ["Genre",]

pick_value_map = {
    'A': 0,
    'Z': 1,
    'M': 2
}

rows_to_drop = ['2020', '2021', '2022', '2023', '2024', '2025']

CATEGORY_MAPPING = {
    'Action': ['action', 'adventure', 'thriller', 'war', 'fight', 'explosion'],
    'Comedy': ['comedy', 'sitcom', 'stand-up', 'parody', 'humor', 'funny'],
    'Drama': ['drama', 'romance', 'documentary', 'biography', 'tragic', 'serious'],
    'Horror': ['horror', 'thriller', 'slasher', 'supernatural', 'psychological', 'ghost'],
    'Romance': ['romance', 'love', 'relationship', 'dating', 'romantic', 'affair'],
    'Sci-Fi': ['science fiction', 'sci-fi', 'space', 'alien', 'future', 'robot', 'cyberpunk'],
    'Animation': ['animation', 'cartoon', 'anime', '3d', 'animated', 'kids'],
    'Thriller': ['thriller', 'suspense', 'mystery', 'crime', 'spy', 'detective'],
    'Martial Arts': ['martial arts', 'kung fu', 'karate', 'taekwondo', 'judo', 'capoeira', 'kickboxing'],
    'Superhero': ['superhero', 'hero', 'comic book', 'marvel', 'dc', 'batman', 'spider-man', 'avengers'],
    'Sports': ['sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'hockey', 'race'],
    'Musical': ['musical', 'song', 'dance', 'musicals', 'performer', 'theatre', 'broadway'],
    'Western': ['western', 'cowboy', 'sheriff', 'outlaw', 'wild west', 'spaghetti western', 'rodeo'],
}

cat_list = keys_list = list(CATEGORY_MAPPING.keys())

cat_features = ['Pick']
numeric_features = ["Time", "RT Crit", "RT Aud", 'Aud #', 'Combo', 'Budget', 'Box Off WW',]
bin_features = [x for x in cat_list]
bin1_features = ['Cost','Pick_0','Pick_1','Pick_2','Pick_3']


model_features = ["RT Aud", 'Box Off WW', 'Cost', 'Pick_0','Pick_1','Pick_2','Pick_3']
actors = ['Nicolas Cage', 'Downtown LA Bridge', 'Sylvester Stallone']

all_vars = ['Pick_0','Pick_1','Pick_2','Comedy']
all_vars = all_vars + numeric_features + actors

csv_file_path = 'data_raw.csv'

name_to_tuple = {
    "Zach": ('y0_test', 'y0_train'),
    "Amin": ('y1_test', 'y1_train'),
    "Mayes": ('y2_test', 'y2_train')
}

z_f = ["RT Crit", 'Box Off WW']
a_f = ["Pick_2", 'Time', "RT Crit", "Nicolas Cage", 'Downtown LA Bridge']
m_f = ["Pick_1", "Comedy", 'Combo', 'Budget', "Downtown LA Bridge"]

best = {
    "Zach": z_f,
    "Amin": a_f,
    "Mayes": m_f
}

dt_params = {
    "Zach": {
        'criterion': 'gini',
        'max_depth': np.int64(9),
        'max_features': np.int64(1),
        'min_samples_leaf': np.int64(1),
        'min_samples_split': np.int64(8),
    },
    "Amin": {
        'criterion': 'gini',
        'max_depth': np.int64(5),
        'max_features': np.int64(7),
        'min_samples_leaf': np.int64(2),
        'min_samples_split': np.int64(18),
    },
    "Mayes": {
        'criterion': 'gini',
        'max_depth': np.int64(6),
        'max_features': np.int64(7),
        'min_samples_leaf': np.int64(3),
        'min_samples_split': np.int64(19),
    }
}


svc_params = {
    "Zach": {
        "C": 1,
        "gamma": 'scale',
        'kernel': 'linear'
    },
    "Amin": {
        "C": 0.1,
        "gamma": 'scale',
        'kernel': 'linear'
    },
    "Mayes": {
        "C": 0.1,
        "gamma": 'scale',
        'kernel': 'linear'
    },
}

best_log_reg_features = {
    "Zach": ['Pick_0','Comedy', 'RT Crit', 'RT Aud', 'Aud #', 'Box Off WW'],
    "Amin": ['Pick_2', 'Time', 'RT Crit', 'RT Aud', 'Box Off WW', 'Nicolas Cage', 'Sylvester Stallone'],
    "Mayes": ['Pick_2', 'Time', 'Combo', 'Downtown LA Bridge', 'Sylvester Stallone']
}