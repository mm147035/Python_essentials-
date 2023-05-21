import pandas as pd
import numpy as np

# Create a DataFrame with random data
np.random.seed(123)
data = {'A': np.random.randn(5),
        'B': np.random.choice(['X', 'Y', 'Z'], 5),
        'C': np.random.randint(1, 100, 5)}
df = pd.DataFrame(data)

print("*******")
# Rename columns
df.rename(columns={'A': 'Column 1', 'B': 'Column 2', 'C': 'Column 3'}, inplace=True)
print(df)

print("*******")
# Filter rows based on a condition and update values in a column
df.loc[df['Column 1'] < 0, 'Column 2'] = 'X'
print(df)

print("*******")
# Create a new column based on conditions
df['Column 4'] = np.where(df['Column 3'] > 50, 'High', 'Low')
print(df)

print("*******")
# Apply a function to multiple columns
df[['Column 1', 'Column 3']] = df[['Column 1', 'Column 3']].apply(lambda x: np.log(x))
print(df)

print("*******")
# Group by multiple columns and calculate aggregate statistics
grouped_df = df.groupby(['Column 2', 'Column 4']).agg({'Column 1': 'mean', 'Column 3': 'sum'})
print(grouped_df)

print("*******")
# Pivot the DataFrame
pivoted_df = df.pivot_table(index='Column 2', columns='Column 4', values='Column 1', aggfunc='mean')
print(pivoted_df)
