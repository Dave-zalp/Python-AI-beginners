# Task : Perform exploratory data analysis on the titanic dataset to understand the survival rates across various features like age,
# gender and class.

# STEPS
# 1. Load the titanic dataset using pandas
# 2. Clean the data by handling missing values (e.g missing age values)
# 3. Explore the dataset
# 4. Visualize the data


import pandas as pd              # Import pandas for data manipulation
import seaborn as sns            # Import seaborn for visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs


# Load the dataset from a CSV file into a pandas DataFrame
data = pd.read_csv('titanic.csv')

# Fill missing values in the 'Age' column
# data['Age'].mean() calculates the average age
# fillna replaces missing (NaN) values with that mean
# inplace=True modifies the original dataset directly
data.fillna({'Age': data['Age'].mean()}, inplace=True)

# Count how many survived (1) and did not survive (0)
# normalize=True converts counts into percentages (proportions)
print(data['Survived'].value_counts(normalize=True))

# Group the dataset by 'Sex' and 'Pclass'
# Then calculate the mean survival rate for each group
# Since Survived is 0 or 1, the mean represents survival probability
print(data.groupby(['Sex', 'Pclass'])['Survived'].mean())

# Create a bar plot showing survival rate by gender
# x='Sex' → categories on x-axis
# y='Survived' → average survival rate on y-axis
# seaborn automatically calculates the mean for each category
sns.barplot(x='Sex', y='Survived', data=data)

# Add a title to the graph
plt.title('Survival rate by Gender')

# Display the plot
plt.show()
