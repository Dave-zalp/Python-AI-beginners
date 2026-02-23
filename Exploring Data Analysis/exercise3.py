# Find the median income from the dataset and create a histogram of income distribution

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset with income column (replace this with your actual dataset)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Income': [50000, 60000, 55000, 75000, 68000]
}

# Step 1: Load the dataset into a DataFrame
df = pd.DataFrame(data)

# Step 2: Find the median income
median_income = df['Income'].median()
print(f"The median income is: {median_income}")

# Step 3: Create a histogram of income distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Income'], bins=5, color='skyblue', edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')

# Display the histogram
plt.axvline(median_income, color='red', linestyle='dashed', linewidth=1.5, label=f'Median: {median_income}')
plt.legend()
plt.show()
