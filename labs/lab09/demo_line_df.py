"""
Demo: Line Chart with DataFrame

This demonstrates how to create a line chart from a DataFrame column.


import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/students.csv")

# Plot Math scores using DataFrame column
plt.plot(df.index, df['Math'])

plt.xlabel("Student Index")
plt.ylabel("Math Score")
plt.title("Math Scores Across Students")

plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("labs/lab09/data/students.csv")
plt.plot(df.index, df['Math'])  # df.index = row numbers (0,1,2...)
plt.xlabel("Student Index")
plt.ylabel("Math Score")
plt.title("Math Scores")
plt.show()