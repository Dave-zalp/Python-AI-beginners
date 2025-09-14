# Pandas is a powerful Python library used for data analysis and data manipulation.
# While NumPy focuses on numerical arrays and matrices,
# Pandas builds on NumPy and introduces labeled data structures,
# making it ideal for working with tabular data (like Excel or SQL tables).

import pandas as pd


# Reading csv files with Pandas
data = pd.read_csv('data-test.csv')
# print(data.head())   # Prints the first few lines of the file

name = data['Name']
# print(name)  # Prints the column (Name)

filtered_data = data[data['Age'] > 18]
# print(filtered_data)  # prints all the data columns where Age is greater than 18.

# print(data.describe())



