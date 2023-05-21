import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emily', 'Kate', 'Sam'],
        'Age': [25, 28, 31, 35],
        'City': ['New York', 'San Francisco', 'Chicago', 'Boston']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

print("*******")
# Accessing column data
print(df['Name'])  # Access the 'Name' column
print(df.Age)  # Alternative way to access the 'Age' column

print("*******")
# Accessing row data
print(df.loc[1])  # Access the second row

print("*******")
# Filtering rows based on a condition
filtered_df = df[df['Age'] > 30]  # Get rows where Age is greater than 30
print(filtered_df)

print("*******")
# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print(df)

print("*******")
# Summary statistics
print(df.describe())
