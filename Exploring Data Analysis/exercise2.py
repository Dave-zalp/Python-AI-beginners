# Create a pie chart to visualize the proportion of passengers who survived vs. those who didn’t in the Titanic dataset.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')

# Count the Survival values
survival_counts = data['Survived'].value_counts()

# print(survival_counts)

plt.pie(survival_counts, labels=['Did not survive', 'Survived'], autopct='%1.1f%%', startangle=90)

plt.title('Proportion of Titanic Survivors')
plt.show()
