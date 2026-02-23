# Questions for this assignment
# Load any other dataset (like the Iris dataset) and perform basic EDA, including handling missing values and visualizing relationships between features.

import pandas as pd  # Import pandas for data manipulation
import seaborn as sns  # Import seaborn for visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs

data = pd.read_csv('iris.csv')

# PERFORMING BASIC EDA

# To view the first row
print(data.head())

# To check the dataset Info
print(data.info())

# Handle missing values (example: fill sepal_width with
data.fillna({'sepal_width': data['sepal_width'].mean()}, inplace=True)

# Visualize the relationship and the feature
sns.scatterplot(x='petal_length', y='petal_width', data=data)
plt.title('Petal Length vs Petal Width')
plt.show()

