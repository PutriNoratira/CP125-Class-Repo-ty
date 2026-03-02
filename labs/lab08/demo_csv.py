# Demo: Working with CSV files
import csv

# Read CSV file
'''print("=== Reading CSV ===")
f = open("labs/lab08/data/students.csv", "r", newline="")
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()'''

'''print("=== Reading CSV ===")
f = open("labs/lab08/data/students.csv", "r", newline="")
reader = csv.reader(f)
content = []
for row in reader:
    content.append(row)

f.close()
print(content)'''

# Write CSV file
'''print("\n=== Writing CSV ===")
f = open("labs/lab08/data/output.csv", "w", newline="")
writer = csv.writer(f)

# Write header
writer.writerow(["Name", "Score", "Grade"])

# Write data
writer.writerow(["Ali", 85, "A"])
writer.writerow(["Sara", 92, "A+"])
writer.writerow(["Ahmad", 78, "B"])

f.close()
print("CSV written to data/output.csv")

print("\n=== Writing CSV ===")
f = open("labs/lab08/data/output.csv", "w", newline="")
writer = csv.writer(f)

# Write header
writer.writerow(["Name", "Score"])

# Write data
writer.writerow(["Ali", 85])
writer.writerow(["Sara", 92])
writer.writerow(["Ahmad", 78])

f.close()'''

import csv

records = [
    ["Name", "Score"],
    ["Ali", 85],
    ["Sara", 92],
    ["Ahmad", 78]
]

f = open("labs/lab08/data/output.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(records)
f.close()