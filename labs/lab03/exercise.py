'''
# Storing 5 student scores
score1 = 85
score2 = 92
score3 = 78
score4 = 88
score5 = 95

# To find the average... we need to manually add each one
total = score1 + score2 + score3 + score4 + score5
average = total / 5
print(f"Average score: {average}")

# Store all scores in ONE list
scores = [85, 92, 78, 88, 95]

# Now we can access individual scores by index
print(f"First score: {scores[0]}")
print(f"Third score: {scores[2]}")
print(f"Last score: {scores[4]}")

scores = [85, 92, 78, 88, 95, 73, 91, 87]
print(f"We now have {scores} scores")

# Creating different types of lists
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
prices = [19.99, 24.50, 15.00]

print(fruits)
print(numbers)
print(prices)

# Different data types
integers = [10, 20, 30, 40, 50]
floats = [1.5, 2.3, 3.7, 4.1]
strings = ["apple", "banana", "cherry"]
booleans = [True, False, True, False]

print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", booleans)

fruits = ["apple", "banana", "kiwi", "durian", "guava", "orange"]

print(fruits[0])  # First element
print(fruits[2])  # Third element
print(fruits[5])  # Sixth element

fruits = ["apple", "banana", "kiwi", "durian", "guava", "orange"]

print(fruits[-1])  # Last element
print(fruits[-2])  # Second-to-last element
print(fruits[-6])  # First element (counting from end)

students = [
    ["Ali", 85, 92],
    ["Sara", 90, 88],
    ["Ahmad", 78, 82]
]

# Access the first student's data
print(students[0])  # ['Ali', 85, 92]

# Access Ali's name
print(students[0][0])  # Ali

# Access Sara's second score
print(students[1][2])  # 88

fruits = ["apple", "banana", "cherry"]
print(fruits[5])  # Only 3 elements, but asking for index 5

numbers = [10, 20, 30]
print(numbers)  # [10, 20, 30]

numbers[1] = 25  # Change the second element
print(numbers)  # [10, 25, 30]
'''