def main():
    # 1. Variables and Data Types: Use a list to store integers
    numbers = []
    
    # 2. Control Structures: Loop for 5 inputs
    for i in range(1, 6):
        val = int(input(f"Enter number {i}: "))
        numbers.append(val)
    
    # 3. Functionality: Sort the list (Ascending)
    numbers.sort()
    print(f"Numbers in ascending order: {numbers}")
    
    # 3. Functionality: Calculate Sum
    total_sum = sum(numbers)
    print(f"Sum of all numbers: {total_sum}")
    
    # 3. Functionality: Find Largest
    largest = max(numbers)
    print(f"Largest number: {largest}")

main()
