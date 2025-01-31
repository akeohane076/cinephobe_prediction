import json
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

from data.constants import numeric_features, bin_features

def count_plot(data, target):
    # sns.countplot(x=target, data=data)
    # plt.title('Target Variable Distribution')
    # plt.show()

    # Get the count of each label (0 vs 1)
    target_counts = data[target].value_counts()
    json_output = json.loads(target_counts.to_json(orient="index",date_format='iso'))

    return json_output

def make_histogram(data, target):
    # for column in numeric_features:
    #     plt.figure(figsize=(10, 6))
    #     sns.histplot(data[data[target] == "Phobe"][column], color='blue', kde=True, label='Phobe')
    #     sns.histplot(data[data[target] == "Phile"][column], color='red', kde=True, label='Phile')
    #     plt.legend()
    #     plt.title(f'Distribution of {column} by Target Variable')
    #     plt.show()
    
    histograms = {}

    for column in numeric_features:
        # Filter the data based on True/False labels
        true_data = data[data[target] == "Phile"][column]
        false_data = data[data[target] == "Phobe"][column]
        bin_edges = np.linspace(data[column].min(),
                            data[column].max(),
                            num=11)
        
        bin_edges = np.round(bin_edges).astype(int)

        # Generate histograms for both True and False subsets using the same bins
        true_hist, _ = np.histogram(true_data, bins=bin_edges)
        false_hist, _ = np.histogram(false_data, bins=bin_edges)

        # Convert histogram data into JSON-friendly format
        histograms[column] = {
            'Phile': {
                'hist': true_hist.tolist(),
                'bins': bin_edges.tolist()
            },
            'Phobe': {
                'hist': false_hist.tolist(),
                'bins': bin_edges.tolist()
            }
        }

    return histograms

def make_box_plots(data, target):
    # for column in numeric_features:
    #     plt.figure(figsize=(10, 6))
    #     sns.boxplot(x=target, y=column, data=data)
    #     plt.title(f'{column} by Target Variable')
    #     plt.show()
    column_json_objects = [{col: data[col].to_json()} for col in data[numeric_features]]

    # Convert to JSON string if needed
    json_output1 = column_json_objects
    return json_output1

def make_count_plots(data, target):
    for column in bin_features:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, hue=target, data=data)
        plt.title(f'{column} by Target Variable')
        plt.show()

        # Calculate the count for each binary variable grouped by target variable
        print(data.groupby(target)[column].value_counts())

def make_heat_map(data, target):
    corr_matrix = data[numeric_features].corr()
    json_output = json.loads(corr_matrix.to_json(orient="index",date_format='iso'))
    return json_output
    # plt.figure(figsize=(12, 8))
    # sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    # plt.title('Correlation Matrix of Numerical Features')
    # plt.show()

    # # Correlation of numerical features with the target variable
    # target_corr = data.corr()[target].sort_values(ascending=False)
    # print(target_corr)

def get_bin_mean(data, target):
    for column in bin_features:
        print(data.groupby(column)[target].mean())