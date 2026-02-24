# ===============================================
# SUPERVISED LEARNING AND DATA PREPARATION
# ===============================================

# In supervised learning:
# - We have INPUT features (X)
# - We have a TARGET/OUTPUT label (y)
# The goal is for the model to learn the relationship between X and y.


# 1️⃣ Import Required Libraries
# pandas is used for handling datasets (CSV files, tables, etc.)
# train_test_split is used to divide the dataset into training and testing sets
import pandas as pd
from sklearn.model_selection import train_test_split

# 2️⃣ Load the Dataset
# read_csv() loads a CSV file into a pandas DataFrame
# A DataFrame is like a table (rows and columns)
data = pd.read_csv('house_prices.csv')

# 3️⃣ Select Features (Independent Variables)
# Features are the input variables that help predict the target.
# Here we assume the dataset contains:
# - Rooms (number of rooms)
# - Size (square footage)
# - Age (age of the house)

# X must be a DataFrame (2D structure)
X = data[['Rooms', 'Size', 'Age']]

# If you select only one column and want it as 2D:
# X = data[['Rooms']]   # Notice double brackets


# 4️⃣ Select Target (Dependent Variable)
# The target is what we want to predict.
# In this case: House Price
# y is usually a Series (1D structure)
y = data['Price']

# 5️⃣ Train-Test Split
# We divide the dataset so the model can be evaluated fairly.
# Why?
# Because testing on the same data used for training leads to overfitting.

# train_test_split parameters:
# - X (features)
# - y (target)
# - test_size=0.2 → 20% of data will be used for testing
# - random_state=42 → ensures reproducibility (same split every time you run it)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# After splitting:
# X_train → features used to train the model
# y_train → correct answers for training
# X_test → unseen features used to evaluate performance
# y_test → correct answers for testing


# 6️⃣ Optional: Check the shape of splits
# This helps confirm the split worked correctly
# print("Training set size:", X_train.shape)
# print("Testing set size:", X_test.shape)


# ===============================================
# IMPORTANT CONCEPT NOTES
# ===============================================

# 🔹 Why Do We Split Data?
# To simulate real-world prediction.
# The model should perform well on data it has NEVER seen before.

# 🔹 What is Overfitting?
# When a model memorizes training data instead of learning patterns.
# It performs well on training data but poorly on test data.

# 🔹 Typical Split Ratios:
# - 80/20 (most common)
# - 70/30
# - 90/10 (for very large datasets)

# 🔹 Next Step After This:
# You would:
# 1. Choose a model (e.g., LinearRegression)
# 2. Fit the model using X_train and y_train
# 3. Predict using X_test
# 4. Evaluate performance (MSE, RMSE, R²)
