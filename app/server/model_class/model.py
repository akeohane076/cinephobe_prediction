import pandas as pd
import numpy as np

from collections import Counter

from data.data_cleaning_functions import groom_data
from sklearn.feature_selection import SelectKBest

from sklearn.svm import SVC

from sklearn.tree import DecisionTreeClassifier

from sklearn.preprocessing import PolynomialFeatures

from sklearn.feature_selection import RFE

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


from charts.charts import count_plot, make_histogram, make_box_plots, make_count_plots, make_heat_map
from data.constants import name_to_tuple, best_log_reg_features, dt_params, svc_params, all_vars, numeric_features
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


class Model:
    def __init__(self, data, target):
        self.data= data
        self.target = target
        self.X_test=data.X_test.drop(["Year", "Pick"], axis=1)
        self.X_train=data.X_train.drop(["Year", "Pick"], axis=1)
        self.y_train=getattr(data, name_to_tuple[target][1])
        self.y_test=getattr(data, name_to_tuple[target][0])
        self.scaler=getattr(data, 'scaler')
        self.best_log_reg_features=best_log_reg_features[target]
        self.k_best_results = []


    def groom_model_data(self, raw_data):
        data = groom_data(raw_data)
        return data

    def describe_data(self):
        print(self.data.describe)

    def get_distribution(self):
        self.distribution = count_plot(self.data.data, self.target)

    def make_histograms(self):
        h = make_histogram(self.data.data, self.target)
        self.histograms = h

    def make_box_plot(self):
        bp = make_box_plots(self.data.data, self.target)

        self.bp = bp

    def count_plots(self):
        make_count_plots(self.data.data, self.target)

    def heat_map(self):
        m = make_heat_map(self.data.data, self.target)
        self.corr_matrix = m

    
    def bin_mean(self):
        make_heat_map(self.data, self.target)

    def decision_tree(self):
        pg = dt_params[self.target]
        dt = DecisionTreeClassifier(criterion=pg['criterion'], max_depth=pg['max_depth'], max_features=pg['max_features'], min_samples_leaf=pg['min_samples_leaf'], min_samples_split=pg['min_samples_split'])
        dt.fit(self.X_train, self.y_train)

        y_pred = dt.predict(self.X_test)

        # Evaluate the model's accuracy on the test set
        test_accuracy = accuracy_score(self.y_test, y_pred)
        print(f"Test Accuracy of Best DecisionTreeClassifier: {test_accuracy}")

        self.opt_dt_score = test_accuracy

        confusion_matr = confusion_matrix(self.y_test, y_pred)

        self.dt_results = {
            'accuracy': test_accuracy,
            'confusion_matrix': confusion_matr.tolist(),
            'y_pred': y_pred.tolist()
        }

    def make_log_reg(self):
            # print(o)
        model = LogisticRegression(solver="liblinear")
        # print(self.X_train.head())
        # Train the model
        model.fit(self.X_train[self.best_log_reg_features], self.y_train)

        # Predict on the test set
        y_pred = model.predict(self.X_test[self.best_log_reg_features])

        # Evaluate the model

        accuracy = accuracy_score(self.y_test, y_pred)
        conf_matrix = confusion_matrix(self.y_test, y_pred)
        # self.conf_matrix = conf_matrix.tolist()
        self.score = accuracy
        self.log_reg_results = {
            'accuracy': accuracy,
            'confusion_matrix': conf_matrix.tolist(),
            'y_pred': y_pred.tolist()
        }
    
    def make_prediction(self, args):
        print(args)

        scaler = self.scaler
        df = pd.DataFrame([args], columns=all_vars)
        
        df = df.where(pd.notnull(df), np.nan)
        df.fillna(0, inplace=True)
        # df_clean = df.dropna()
        print(df) 
        print(self.X_train)
        df[numeric_features] = scaler.fit_transform(df[numeric_features])
        model = LogisticRegression(solver="liblinear")
        # print(self.X_train.head())
        # Train the model
        model.fit(self.X_train[self.best_log_reg_features], self.y_train)

        # Predict on the test set
        y_pred = model.predict(df[self.best_log_reg_features])
        self.movie_prediction = y_pred.tolist()


    def random_forrest(self):
        i = 2
        scores = []
        while i < 20:

            rf = RandomForestClassifier(n_estimators=100)
            rf.fit(self.X_train, self.y_train)

            # Get feature importances
            importances = rf.feature_importances_

            # Sort features by importance
            indices = np.argsort(importances)[::-1]

            # Select top 10 features
            top_features = self.X_train.columns[indices[:i]]
            X_selected = self.X_train[top_features]
            logreg = LogisticRegression(solver="liblinear", max_iter=200)
            logreg.fit(X_selected, self.y_train)

            # Transform the test set using the selected features
            X_test_selected = self.X_test[top_features]

            # Make predictions on the test set
            y_pred = logreg.predict(X_test_selected)
            accuracy = accuracy_score(self.y_test, y_pred)
            scores.append((i,accuracy))
            i += 1
        self.rf_scores = scores

        print(accuracy)

    def ada_boost(self):
        base_learner = DecisionTreeClassifier(max_depth=7)

        # Create an AdaBoost model using the decision tree as the base learner
        ada_boost = AdaBoostClassifier(estimator=base_learner, n_estimators=100, random_state=42)
        ada_boost.fit(self.X_train, self.y_train)

        y_pred = ada_boost.predict(self.X_test)

        # Evaluate the model's accuracy
        accuracy = accuracy_score(self.y_test, y_pred)
        self.ada_boost_score = accuracy
        confusion_matr = confusion_matrix(self.y_test, y_pred)

        self.ada_boost_results = {
            'accuracy': accuracy,
            'confusion_matrix': confusion_matr.tolist(),
            'y_pred': y_pred.tolist()
        }

    def get_kbest(self):
        best = 0
        i = 2
        while i < 20:
            log_reg = LogisticRegression(max_iter=200)
            selector = SelectKBest(k=i)
            X_selected = selector.fit_transform(self.X_train, self.y_train)
            log_reg.fit(X_selected, self.y_train)

            # Transform the test set to match the selected features from the training set
            X_test_selected = selector.transform(self.X_test)

            # Make predictions on the test set
            y_pred = log_reg.predict(X_test_selected)

            # Evaluate the model's accuracy
            accuracy = accuracy_score(self.y_test, y_pred)
            # print("Accuracy with selected features:", accuracy)
            selected_indices = selector.get_support(indices=True)

            # Display the selected feature names
            selected_features = self.X_test.columns
            selected_feature_names = [selected_features[i] for i in selected_indices]
            # print(selected_feature_names)
            if accuracy > best:
                best = accuracy
                self.k_best_score = accuracy
                self.k_best_features = selected_feature_names
                self.k_best_y_pred = y_pred.tolist(),

            confusion_matr = confusion_matrix(self.y_test, y_pred)

            self.k_best_results.append({
                'accuracy': accuracy,
                'y_pred': y_pred.tolist(),
                'confusion_matrix': confusion_matr.tolist(),
                'num_features': i
            })
            i += 1


    def find_best_log_reg(self):
        best = 0
        best_f = []
        for o_i in self.data.options:
            o = o_i
            # print(o)
            model = LogisticRegression(solver="liblinear")
            # print(self.X_train.head())
            # Train the model
            model.fit(self.X_train[o], self.y_train)

            # Predict on the test set
            y_pred = model.predict(self.X_test[o])

            # Evaluate the model

            accuracy = accuracy_score(self.y_test, y_pred)
            if accuracy > best:
                best = accuracy
                best_f = o
        self.best = best
        self.best_f = best_f
        self.X_test = self.X_test[best_f]
        self.X_train = self.X_train[best_f]

    def get_rfe(self):
        best= 0
        i = 2
        scores = []
        while i < 20:
            log_reg = LogisticRegression()
            selector = RFE(log_reg, n_features_to_select=i)
            X_selected = selector.fit_transform(self.X_train, self.y_train)

            log_reg.fit(X_selected, self.y_train)

            X_test_selected = selector.transform(self.X_test)

            y_pred = log_reg.predict(X_test_selected)
            accuracy = accuracy_score(self.y_test, y_pred)
            confusion_matr = confusion_matrix(self.y_test, y_pred)

            selected_indices = selector.get_support(indices=True)

            # Display the selected feature names
            selected_features = self.X_test.columns
            selected_feature_names = [selected_features[i] for i in selected_indices]

            if accuracy > best:
                best = accuracy
                self.rfe_score = accuracy
                self.rfe_best_features = selected_feature_names
                self.rfe_best_y_pred = y_pred.tolist()
            scores.append({
                'num_features': i,
                'accuracy': accuracy,
                'confusion_matrix': confusion_matr.tolist(),
                'y_pred': y_pred.tolist()
            })
            i += 1
        self.rfe_scores = scores
    
    def random_forrest(self):
        best = 0
        i = 2
        scores = []
        while i < 20:

            rf = RandomForestClassifier(n_estimators=1000)
            rf.fit(self.X_train, self.y_train)

            # Get feature importances
            importances = rf.feature_importances_

            # Sort features by importance
            indices = np.argsort(importances)[::-1]

            top_features = self.X_train.columns[indices[:i]]
            X_selected = self.X_train[top_features]
            logreg = LogisticRegression(solver="liblinear", max_iter=200)
            logreg.fit(X_selected, self.y_train)

            # Transform the test set using the selected features
            X_test_selected = self.X_test[top_features]

            # Make predictions on the test set
            y_pred = logreg.predict(X_test_selected)
            accuracy = accuracy_score(self.y_test, y_pred)

            confusion_matr = confusion_matrix(self.y_test, y_pred)

            if accuracy > best:
                best = accuracy
                self.rf_score = accuracy
                self.rf_best_features = top_features.tolist()
                self.rf_best_y_pred = y_pred.tolist(),

            scores.append({
                'num_features': i,
                'accuracy': accuracy,
                'y_pred': y_pred.tolist(),
                'best_features': top_features.tolist(),
                'confustion_matrix': confusion_matr.tolist()
            })
            i += 1
        self.rf_scores = scores
    
    def svc(self):
        pg = svc_params[self.target]
        svc_model = SVC(C=pg['C'], gamma=pg['gamma'], kernel=pg['kernel'])
        svc_model.fit(self.X_train, self.y_train)

        y_pred = svc_model.predict(self.X_test)

        accuracy = accuracy_score(self.y_test, y_pred)
        print(f"Optimized Accuracy: {accuracy * 100:.2f}%")
        confusion_matr = confusion_matrix(self.y_test, y_pred)
        print(confusion_matr)
        self.svc_score = accuracy

        self.svc_results = {
            'accuracy': accuracy,
            'confusion_matrix': confusion_matr.tolist(),
            'y_pred': y_pred.tolist()
        }

    def poly_preprocess(self):
        poly = PolynomialFeatures(degree=2)

        # Transform the training and test sets to include polynomial features
        X_train_poly = poly.fit_transform(self.X_train)
        X_test_poly = poly.transform(self.X_test)

        # Initialize the Logistic Regression model
        logreg = LogisticRegression(max_iter=200)

        # Train the Logistic Regression model on the polynomial features
        logreg.fit(X_train_poly, self.y_train)

        # Make predictions on the test set
        y_pred = logreg.predict(X_test_poly)

        # Evaluate the model's accuracy
        accuracy = accuracy_score(self.y_test, y_pred)
        self.poly_score = accuracy

        confusion_matr = confusion_matrix(self.y_test, y_pred)

        self.ply_results = {
            'accuracy': accuracy,
            'confusion_matrix': confusion_matr.tolist(),
            'y_pred': y_pred.tolist()
        }

    def combined_model(self):
        # list1 = 
        lists = [
            self.ada_boost_results['y_pred'],
            self.dt_results['y_pred'],
            self.log_reg_results['y_pred'],
            self.svc_results["y_pred"],
            self.ply_results["y_pred"],
            # self.rf_best_y_pred,
            getattr(self, 'rfe_best_y_pred')
            # self.rfe_best_y_pred,
            # self.k_best_y_pred
        ]
        zipped = zip(*lists)

        aggregated = [Counter(group).most_common(1)[0][0] for group in zipped]
        accuracy = accuracy_score(self.y_test, aggregated)

        self.combined_accuracy = accuracy
