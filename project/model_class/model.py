import pandas as pd

import numpy as np

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.preprocessing import PolynomialFeatures

from data.data_cleaning_functions import groom_data


from charts.charts import count_plot, make_histogram, make_box_plots, make_count_plots, make_heat_map, get_bin_mean
from data.constants import keep, target, cat_features, numeric_features, bin_features, model_features, name_to_tuple, all_vars, best_target_features, best_log_reg_features
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


class Model:
    def __init__(self, data, target):
        self.data= data
        self.target = target
        self.X_test=data.X_test[all_vars]
        self.X_train=data.X_train[all_vars]
        self.y_train=getattr(data, name_to_tuple[target][1])
        self.y_test=getattr(data, name_to_tuple[target][0])


    def groom_model_data(self, raw_data):
        data = groom_data(raw_data)
        return data

    def describe_data(self):
        print(self.data.describe)

    def get_distribution(self, target):
        count_plot(self.data, target)

    def make_histograms(self, target):
        make_histogram(self.data, target)

    def make_box_plot(self, target):
        make_box_plots(self.data, target)

    def count_plots(self, target):
        make_count_plots(self.data, target)

    def heat_map(self, target):
        make_heat_map(self.data, target)
    
    def bin_mean(self, target):
        make_heat_map(self.data, target)

    def best_decision_tree(self):
        param_grid = {
            'criterion': ['gini', 'entropy'],
            'max_depth': [None] + list(np.arange(1,21)),
            'min_samples_split': np.arange(2,20),
            'min_samples_leaf': np.arange(1,4),
            'max_features': [None, 'sqrt', 'log2'] + list(np.arange(1, self.X_train.shape[1] + 1)),
        }

        dt = DecisionTreeClassifier(random_state=42)

        grid_search = GridSearchCV(estimator=dt, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

        # Fit the grid search to the training data
        grid_search.fit(self.X_train, self.y_train)

        # Get the best parameters and best score from GridSearchCV
        best_params = grid_search.best_params_
        best_score = grid_search.best_score_

        # Print the best hyperparameters
        print("Best Hyperparameters found by GridSearchCV:", best_params)
        print("Best Cross-Validation Accuracy:", best_score)

        # Train the best DecisionTree model on the full training data
        best_dt = grid_search.best_estimator_

        # Make predictions on the test set
        y_pred = best_dt.predict(self.X_test)

        # Evaluate the model's accuracy on the test set
        test_accuracy = accuracy_score(self.y_test, y_pred)
        print(f"Test Accuracy of Best DecisionTreeClassifier: {test_accuracy}")

        self.opt_dt_score = test_accuracy

        confusion_matr = confusion_matrix(self.y_test, y_pred)


        # self.opt_dt_results = {
        #     accuracy_score: test_accuracy,
        #     confusion_matrix: confusion_matr.tolist(),
        #     y_pred: y_pred.tolist()
        # }


    def random_forrest(self):
        i = 2
        scores = []
        while i < 14:

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


    def get_l1(self):
        log_reg = LogisticRegression(penalty='l1', solver='liblinear')
        log_reg.fit(self.X_train, self.y_train)

        y_pred = log_reg.predict(self.X_test)   
        accuracy = accuracy_score(self.y_test, y_pred)

        self.l1 = accuracy


        log_reg2 = LogisticRegression(penalty='l2', solver='liblinear')
        log_reg2.fit(self.X_train, self.y_train)

        y_pred2 = log_reg2.predict(self.X_test)   
        accuracy2 = accuracy_score(self.y_test, y_pred2)

        self.l2 = accuracy2

    def get_svc(self):
        param_grid = {
            'C': [0.1, 1, 10, 100],
            'gamma': ['scale', 'auto'],
            'kernel': ['rbf', 'linear']
        }

        # Create the SVC model
        svc_model = SVC()

        # Perform GridSearchCV to find the best parameters
        grid_search = GridSearchCV(svc_model, param_grid, cv=5)
        grid_search.fit(self.X_train, self.y_train)

        # Get the best hyperparameters
        print("Best parameters found: ", grid_search.best_params_)

        # Make predictions using the best model
        best_svc = grid_search.best_estimator_
        y_pred = best_svc.predict(self.X_test)

        # Evaluate the model's accuracy
        accuracy = accuracy_score(self.y_test, y_pred)
        # print(f"Optimized Accuracy: {accuracy * 100:.2f}%")
        confusion_matr = confusion_matrix(self.y_test, y_pred)
        # print(confusion_matr)
        self.svc_score = accuracy


    def ada_boost(self):
        base_learner = DecisionTreeClassifier(max_depth=7)

        # Create an AdaBoost model using the decision tree as the base learner
        ada_boost = AdaBoostClassifier(estimator=base_learner, n_estimators=100, random_state=42)
        ada_boost.fit(self.X_train, self.y_train)

        y_pred = ada_boost.predict(self.X_test)

        # Evaluate the model's accuracy
        accuracy = accuracy_score(self.y_test, y_pred)
        self.ada_boost_score = accuracy


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

    def get_kbest(self):
        best = 0
        i = 2
        while i < 14:
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
            
            i += 1

    def get_rfe(self):
        i = 2
        scores = []
        while i < 15:
            log_reg = LogisticRegression()
            selector = RFE(log_reg, n_features_to_select=i)
            X_selected = selector.fit_transform(self.X_train, self.y_train)

            log_reg.fit(X_selected, self.y_train)

            X_test_selected = selector.transform(self.X_test)

            y_pred = log_reg.predict(X_test_selected)
            accuracy = accuracy_score(self.y_test, y_pred)
            scores.append((i,accuracy))
            # print(accuracy)
            i += 1
        self.rfe_scores = scores


    def make_log_reg(self):
        a = self.data.a_data["Cast / Crew"]
        bf = best_log_reg_features[self.target]

        a_1 = a.tolist()
        a_2 = bf + a_1

        model = LogisticRegression(solver="liblinear")
        # print(self.X_train.head())
        # Train the model
        model.fit(self.X_train[bf], self.y_train)

        # Predict on the test set
        y_pred = model.predict(self.X_test[bf])

        # Evaluate the model

        accuracy = accuracy_score(self.y_test, y_pred)
        print(accuracy)
        self.best = accuracy


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
        # self.X_test = self.X_test[best_f]
        # self.X_train = self.X_train[best_f]

    def opt_log_reg(self):

        # Initialize LogisticRegression
        log_reg = LogisticRegression()

        # Define a grid of hyperparameters
        param_grid = {
            'C': np.logspace(-3, 3, 7),  # Regularization strength: from 0.001 to 1000
            'penalty': ['l1', 'l2'],  # Regularization type: l1 (Lasso), l2 (Ridge)
            'solver': ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'],  # Optimization solvers
            'max_iter': [100, 200, 300],  # Maximum number of iterations for convergence
            'fit_intercept': [True, False],  # Whether to include an intercept term
            'class_weight': [None, 'balanced']  # Weighting of classes for imbalanced datasets
        }

        # Set up GridSearchCV
        grid_search = GridSearchCV(estimator=log_reg, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

        # Fit the grid search to the training data
        grid_search.fit(self.X_train[best_log_reg_features[self.target]], self.y_train)

        # Get the best parameters and best score from GridSearchCV
        best_params = grid_search.best_params_
        best_score = grid_search.best_score_

        # Print the best hyperparameters
        print("Best Hyperparameters found by GridSearchCV:", best_params)
        print("Best Cross-Validation Accuracy:", best_score)

        # Train the best LogisticRegression model on the full training data
        best_log_reg = grid_search.best_estimator_

        # Make predictions on the test set
        y_pred = best_log_reg.predict(self.X_test[best_log_reg_features[self.target]])

        # Evaluate the model's accuracy on the test set
        test_accuracy = accuracy_score(self.y_test, y_pred)
        print(f"Test Accuracy of Best LogisticRegression: {test_accuracy}")

        self.opt_log_reg_score = test_accuracy

