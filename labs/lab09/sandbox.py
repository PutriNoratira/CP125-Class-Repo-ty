"""
Sandbox for experimenting with DataFrames

Use this file to try out different DataFrame operations
as you work through the lab.


import pandas as pd

# Example: Create a simple DataFrame
students = pd.DataFrame({
    'Name': ["Ali", "Sara", "Ahmad", "Fatimah"],
    'Math': [85, 92, 78, 88],
    'Science': [78, 88, 82, 91]
})

print(students)
print(f"\nAverage Math: {students['Math'].mean()}")
"""

import pandas as pd

df = pd.DataFrame({
    'Name': ["Ali", "Sara", "Ahmad", "Fatimah"],
    'Math': [85, 92, 78, 88],
    'Science': [78, 88, 82, 91],
    'Score': [85, 92, 89, 98]
})
print(df)

print(df.shape)      # (25, 6)
print(df.columns)    # Index(['StudentID', 'Name', ...])
print(list(df.columns))  # ['StudentID', 'Name', ...]

df.loc[2]                          # Single row
df.loc[1:3]                        # Rows 1, 2, 3 (INCLUSIVE)
df.loc[:, ['Math', 'Science']]     # All rows, specific columns
df.loc[df['Math'] > 80]            # Conditional selection
df.loc[df['Math'] > 80, ['Name']]  # Condition + specific columns

df.iloc[2]          # Row at position 2
df.iloc[1:3]        # Rows 1, 2 (EXCLUSIVE of 3)
df.iloc[1:3, 0:2]   # Rows 1-2, columns 0-1