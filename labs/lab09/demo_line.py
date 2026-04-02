"""
Demo: Your First Line Chart

This demonstrates how to create a basic line chart using matplotlib.


import matplotlib.pyplot as plt

# Sample data: Student numbers and their Math scores
students = [1, 2, 3, 4, 5]
scores = [85, 92, 78, 88, 95]

# Create the line chart
plt.plot(students, scores)

# Add labels
plt.xlabel("Student Number")
plt.ylabel("Math Score")
plt.title("Math Score Trends")

# Display the chart
plt.show()
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [85, 92, 78, 88, 95]

plt.plot(x, y)              # Create line (x=horizontal, y=vertical)
plt.xlabel("Student Number") # Label x-axis
plt.ylabel("Math Score")     # Label y-axis
plt.title("Math Scores")     # Add title
plt.show()                   # Display (required!)
