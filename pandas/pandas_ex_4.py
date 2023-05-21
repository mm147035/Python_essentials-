import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emily', 'Kate', 'Sam', 'Alex'],
        'Age': [25, 28, 31, 35, 24],
        'City': ['New York', 'San Francisco', 'Chicago', 'Boston', 'Los Angeles'],
        'Salary': [50000, 60000, 70000, 80000, 55000],
        'Department': ['Sales', 'Marketing', 'Finance', 'HR', 'IT']}
df = pd.DataFrame(data)

# Sorting the DataFrame by multiple columns
sorted_df = df.sort_values(by=['Department', 'Age'], ascending=[True, False])
print(sorted_df)

# Counting the occurrences of values in a column
city_counts = df['City'].value_counts()
print(city_counts)

# Selecting rows based on multiple conditions
selected_rows = df[(df['Age'] > 25) & (df['Salary'] < 60000)]
print(selected_rows)

# Creating a new DataFrame by selecting specific rows and columns
new_df = df.loc[df['Department'].isin(['Sales', 'Finance']), ['Name', 'Age', 'Department']]
print(new_df)

# Applying a custom function to create a new column
def age_group(age):
    if age < 30:
        return 'Young'
    elif age < 40:
        return 'Mid-aged'
    else:
        return 'Old'

df['Age Group'] = df['Age'].apply(age_group)
print(df)

# Grouping by a column and aggregating multiple columns with custom functions
grouped_df = df.groupby('Department').agg({'Salary': 'mean', 'Age': ['min', 'max']})
print(grouped_df)
