# Modify the above code to read a CSV file, select specific columns, and write the output to a new CSV file.
import pandas as pd

df = pd.read_csv('data-test.csv')

selected_columns = df[['City', 'Age']]

new_file = 'output.csv'

selected_columns.to_csv(new_file, index=False)
