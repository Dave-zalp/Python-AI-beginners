import pandas as pd


# LOADING AND INSPECTING DATA
data = pd.read_csv('MBA.csv')

# print(data.head())

# To get the shape of the data
# print(data.shape)

# To print the data coluns
# print(data.columns)

# To get the info of the data there
# print(data.info())



# HANDLING MISSING DATA

# To check the data and return the sum of null values in each column
# print(data.isnull().sum())


# To drop missing data
# data_clean = data.dropna()

# Now after dropping missing data, we can run the script to check for the null/missing data
# And it would return no missing data found
# print(data_clean.isnull().sum())

# To replace the missing values in 'work_experience' column with the mean of the 'work_experience' column
data.fillna({'work_exp': data['work_exp'].mean()}, inplace=True)


# DATA TRANSFORMATION AND FEATURE ENGINEERING
# DATA TRANSFORMATION involves modifying your data to meet the requirements of machine learning model.
# Transforming the data ensures consistency and improves the model accuracy.

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

data[['Age', 'Income']] = scaler.fit_transform(data[['Age', 'Income']])


# Categorical data encoding (one-hot encoding)
# One-hot encoding converts the categorical variables into a set of binary columns (Os and 1s)
# Where each category becomes its own column
data_encoded = pd.get_dummies(data, columns=['Gender', 'Purchased'])


