# This program uses the Pandas library to read and manipulate data from a CSV file.

import pandas as pd

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv('example.csv')

# Print the first five rows of the DataFrame
print(data.head())

# Calculate the average value of the 'price' column
avg_price = data['price'].mean()

# Print the average price
print("Average price:", avg_price)
