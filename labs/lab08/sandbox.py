# Lab 08 Sandbox - Follow along with the lab instructions

# Step 1: The Problem - Data doesn't persist
'''scores = []
scores.append(85)
scores.append(92)
scores.append(78)

print("Scores:", scores)'''

# Try running this program again - scores will be empty!

'''print (scores)'''

# Write scores to a file
'''f = open("labs/lab08/data/scores.txt", "w")
f.write("85\n")
f.write("92\n")
f.write("78\n")
f.close()

print("Scores saved to file!")'''

# Read scores from the file
'''f = open("labs/lab08/data/scores.txt", "r")
data = f.read()
print(data)
f.close()'''

# Read
f = open("labs/lab08/data/scores.txt", "r")
lines = f.readlines()
f.close()

# Process
scores = []
for line in lines:
    score = int(line.strip())
    scores.append(score)

average = sum(scores) / len(scores)

# Write
f = open("labs/lab08/data/report.txt", "w")
f.write(f"Average: {average}\n")
f.close()
