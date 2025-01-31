import seaborn as sns
import matplotlib.pyplot as plt

from data.constants import numeric_features, bin_features

def count_plot(data, target):
    sns.countplot(x=target, data=data)
    plt.title('Target Variable Distribution')
    plt.show()

    # Get the count of each label (0 vs 1)
    target_counts = data[target].value_counts()
    print(target_counts)

def make_histogram(data, target):
    for column in numeric_features:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[data[target] == "Phobe"][column], color='blue', kde=True, label='Phobe')
        sns.histplot(data[data[target] == "Phile"][column], color='red', kde=True, label='Phile')
        plt.legend()
        plt.title(f'Distribution of {column} by Target Variable')
        plt.show()

def make_box_plots(data, target):
    for column in numeric_features:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=target, y=column, data=data)
        plt.title(f'{column} by Target Variable')
        plt.show()

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
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix of Numerical Features')
    plt.show()

    # Correlation of numerical features with the target variable
    target_corr = data.corr()[target].sort_values(ascending=False)
    print(target_corr)

def get_bin_mean(data, target):
    for column in bin_features:
        print(data.groupby(column)[target].mean())