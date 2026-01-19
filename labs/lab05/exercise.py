'''coordinates = (3.14, 101.68)
coordinates[0] = 0  # TypeError: 'tuple' object does not support item assignment

single = (5,)   # Correct: tuple with one element
wrong = (5)     # Wrong: just the integer 5

print(type(single))  # <class 'tuple'>
print(type(wrong))   # <class 'int'>

colors = ("red", "green", "blue", "yellow")

# Indexing
print(colors[0])    # red
print(colors[-1])   # yellow

# Slicing
print(colors[1:3])  # ('green', 'blue')

# Membership
print("red" in colors)  # True

# Length
print(len(colors))  # 4

point = (3.14, 101.68)

# Using indexing (clunky)
x = point[0]
y = point[1]

# Using unpacking (clean and professional)
x, y = point

print(x)  # 3.14
print(y)  # 101.68

results = [("A", 90), ("B", 85)]

for name, score in results:
    print(f"Student {name} got {score}")

scores = (90, 80, 85)
# Use sorted() function, NOT scores.sort()
sorted_scores = sorted(scores)
print(sorted_scores)  # [80, 85, 90] (This is now a list)

# A list of student records
# Each record is (name, score, attendance_percent)
students = (
    ("Ali", 85, 95),
    ("Sara", 92, 98),
    ("Ahmad", 78, 80)
)

# Accessing nested data
first_student = students[0]
print(first_student)        # ("Ali", 85, 95)
print(first_student[0])     # "Ali"

# Or using unpacking in a loop (preferred)
for name, score, attendance in students:
    if attendance < 90:
        print(f"Warning: {name} has low attendance")

passing_scores = []

all_scores = [45, 82, 67, 91, 55, 78, 88]

for score in all_scores:
    if score >= 60:
        passing_scores.append(score)

print(passing_scores)  # [82, 67, 91, 78, 88]

words = ["hi", "go", "apple", "me", "cat", "banana"]

for word in words:
    if len(word) < 3:
        words.remove(word)

print(words)  # ["go", "apple", "cat", "banana"] — "go" was skipped!

words = ["hi", "go", "apple", "me", "cat", "banana"]

for word in words[:]:  # [:] creates a copy
    if len(word) < 3:
        words.remove(word)

print(words)  # ["apple", "cat", "banana"] — Correct!'''

words = ["hi", "go", "apple", "me", "cat", "banana"]
result = []

for word in words:
    if len(word) >= 3:
        result.append(word)

print(result)  # ["apple", "cat", "banana"]