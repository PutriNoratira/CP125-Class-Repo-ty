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
print(y)  # 101.68'''

results = [("A", 90), ("B", 85)]

for name, score in results:
    print(f"Student {name} got {score}")