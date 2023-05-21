# This program reads a CSV file and performs some basic data analysis using pandas.

import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv("sales_data.csv")

# Print the first few rows of the dataframe
print(df.head())

# Get basic statistics for the data
print(df.describe())

# Group the data by product and calculate the total revenue for each product
revenue_by_product = df.groupby("product")["revenue"].sum()
print(revenue_by_product)

# Calculate the total revenue for each month
revenue_by_month = df.groupby("month")["revenue"].sum()
print(revenue_by_month)

# Calculate the average revenue per sale
avg_revenue_per_sale = df["revenue"].mean()
print(avg_revenue_per_sale)
