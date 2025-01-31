from data.data_cleaning_functions import groom_data
import itertools

from data.constants import numeric_features, bin_features, all_vars, target

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

class Data:
    def __init__(self,raw_data, actor_raw_data):
        self.raw_data = raw_data
        self.a_r_data= actor_raw_data
        self.data = self.groom_model_data(raw_data)
        self.options = self.make_feature_options()
        self.a_data = self.groom_actor_data(actor_raw_data)

    def groom_actor_data(self, ad):
        l = ["Cast / Crew", "Appearances"]
        d = ad[l]
        return d

    def add_actors(self):

        m = self.data
        for _, actor_row in self.a_data.iterrows():
            actor_name = actor_row["Cast / Crew"]
            actor_movies = actor_row['Appearances']
            
            # Add a binary column for each actor in the 'movies' DataFrame
            m[actor_name] = m['Movie'].apply(lambda movie: 1 if movie in actor_movies else 0)
        m = m.drop(columns="Movie")
        self.data = m

    def groom_model_data(self, raw_data):
        data = groom_data(raw_data)
        return data

    def split_data(self):
        df = self.data
        y0 = df[target[0]]
        y1 = df[target[1]]
        y2 = df[target[2]]
        X = df.drop(target, axis=1)
        X_train, X_test, y0_train, y0_test, y1_train, y1_test, y2_train, y2_test = train_test_split(X, y0, y1, y2, test_size=0.20, random_state=42)
        print('done')

        scaler = StandardScaler()

        X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
        X_test[numeric_features] = scaler.fit_transform(X_test[numeric_features])

        self.X_test=X_test
        self.X_train=X_train
        self.y0_train=y0_train
        self.y1_train=y1_train
        self.y2_train=y2_train
        self.y0_test=y0_test
        self.y1_test=y1_test
        self.y2_test=y2_test

    def make_feature_options(self):
        all_combinations = []
        
        # Generate combinations for all possible lengths (from 1 to len(arr))
        for r in range(1, len(all_vars) + 1):
            # itertools.combinations generates combinations of length r
            combinations = itertools.combinations(all_vars, r)
            all_combinations.extend(combinations)
        
        return [list(t) for t in all_combinations]