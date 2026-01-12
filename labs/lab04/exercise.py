'''scores = [85, 92, 78, 88, 95]
count = len(scores)
print(f"Number of scores: {count}")  # Output: 5

temperatures = [28, 32, 25, 35, 30]

lowest = min(temperatures)
highest = max(temperatures)

print(f"Lowest: {lowest}")   # Output: 25
print(f"Highest: {highest}") # Output: 35

prices = [19.99, 24.50, 15.00, 32.00]
total = sum(prices)
print(f"Total: ${total:.2f}")  # Output: $91.49

scores = [85, 92, 78, 88, 95]

total = sum(scores)
count = len(scores)
average = total / count

print(f"Average: {average}")  # Output: 87.6

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # [2, 4, 6, 8, 10]'''

all_scores = [45, 82, 67, 91, 55, 78, 88]
passing_scores = []

for score in all_scores:
    if score >= 60:
        passing_scores.append(score)

print(f"Passing scores: {passing_scores}")  # [82, 67, 91, 78, 88]
print(f"Count: {len(passing_scores)}")      # 5