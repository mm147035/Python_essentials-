import pandas as pd

# Create a DataFrame with student data
data = {'Name': ['John', 'Emily', 'Kate', 'Sam', 'Daniel'],
        'Age': [20, 22, 21, 19, 23],
        'City': ['New York', 'San Francisco', 'Chicago', 'Boston', 'Los Angeles'],
        'GPA': [3.5, 3.2, 3.8, 3.6, 3.9],
        'Major': ['Computer Science', 'Physics', 'Mathematics', 'Chemistry', 'Engineering']}
df = pd.DataFrame(data)

print("*******")
# Selecting rows based on multiple conditions
selected_df = df[(df['City'] == 'New York') & (df['GPA'] > 3.5)]
print(selected_df)

print("*******")
# Sorting the DataFrame by multiple columns
sorted_df = df.sort_values(['City', 'Age'], ascending=[True, False])
print(sorted_df)

print("*******")
# Extracting unique values from a column
unique_majors = df['Major'].unique()
print(unique_majors)

print("*******")
# Counting occurrences of each value in a column
major_counts = df['Major'].value_counts()
print(major_counts)

print("*******")
# Applying a custom function to a column and creating a new column based on the result
def is_honors(gpa):
    if gpa >= 3.5:
        return 'Yes'
    else:
        return 'No'

df['Honors'] = df['GPA'].apply(is_honors)
print(df)

print("*******")
# Grouping and summarizing data with aggregate functions
grouped_df = df.groupby('Major').agg({'Age': 'mean', 'GPA': ['min', 'max']})
print(grouped_df)
