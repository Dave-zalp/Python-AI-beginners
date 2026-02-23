# Visualising data with Matplotib and Seaborn
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('MBA.csv')

# Plot
plt.plot(data['Age'], data['Income'])

# Title of the plot
plt.title('Age Vs Income')

# x-axis Label
plt.xlabel('Age')

# y-axis Label
plt.ylabel('Income')

# Show the graph plot
plt.show()
