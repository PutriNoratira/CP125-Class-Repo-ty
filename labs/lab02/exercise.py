'''# Define the function once
def calculate_bill(meal_price):
    tax = meal_price * 0.08  # 6% SST tax
    service_charge = 2.00
    total = meal_price + tax + service_charge
    return total

# Now reuse it for each customer
total1 = calculate_bill(8.50)  # Nasi Lemak
print(f"Customer 1 total: RM{total1:.2f}")

total2 = calculate_bill(3.50)  # Roti Canai
print(f"Customer 2 total: RM{total2:.2f}")

total3 = calculate_bill(7.00)  # Mee Goreng
print(f"Customer 3 total: RM{total3:.2f}")

# Rectangle 1
length1 = 5
width1 = 3
area1 = length1 * width1
print(f"Rectangle 1: {area1}")

# Rectangle 2
length2 = 10
width2 = 4
area2 = length2 * width2
print(f"Rectangle 2: {area2}")

# Rectangle 3
length3 = 7
width3 = 2
area3 = length3 * width3
print(f"Rectangle 3: {area3}")

def calculate_rectangle_area(length, width):  # Both change, so both are parameters
    area = length * width  # Formula stays the same
    return area

# Now call with different values
print(f"Rectangle 1: {calculate_rectangle_area(5, 3)}")
print(f"Rectangle 2: {calculate_rectangle_area(10, 4)}")
print(f"Rectangle 3: {calculate_rectangle_area(7, 2)}")

# Student 1
name1 = "Ahmad"
marks1 = 85
print(f"{name1} scored {marks1} marks")

# Student 2
name2 = "Fatimah"
marks2 = 92
print(f"{name2} scored {marks2} marks")

def display_score(name, marks):  # Two parameters for two changing values
    print(f"{name} scored {marks} marks")

display_score("Ahmad", 85)
display_score("Fatimah", 92)

def add_with_print(a, b):
    result = a + b
    print(result)  # Displays the number on screen

def add_with_return(a, b):
    result = a + b
    return result  # Gives back the number

# Test 1: Using print
x = add_with_print(5, 3)
print(f"x contains: {x}")

# Test 2: Using return
y = add_with_return(5, 3)
print(f"y contains: {y}")

def calculate_discount(price):
    return price * 0.10  # Returns 10% of price

original_price = 100.00
discount_amount = calculate_discount(original_price)
final_price = original_price - discount_amount
print(f"Final price: RM{final_price:.2f}")

# Calculating areas without factorization
pi = 3.14159

# Circle 1
radius1 = 5
area1 = pi * radius1 * radius1
print(f"Circle 1 (radius {radius1}): Area = {area1:.2f}")

# Circle 2
radius2 = 10
area2 = pi * radius2 * radius2
print(f"Circle 2 (radius {radius2}): Area = {area2:.2f}")

# Circle 3
radius3 = 7
area3 = pi * radius3 * radius3
print(f"Circle 3 (radius {radius3}): Area = {area3:.2f}")

def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

# Now the calculation is defined once and reused
area1 = calculate_circle_area(5)
print(f"Circle 1 (radius 5): Area = {area1:.2f}")

area2 = calculate_circle_area(10)
print(f"Circle 2 (radius 10): Area = {area2:.2f}")

area3 = calculate_circle_area(7)
print(f"Circle 3 (radius 7): Area = {area3:.2f}")

def process_student():
    # Responsibility 1: Getting input
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    
    # Responsibility 2: Making decision
    if score >= 50:
        status = "Pass"
    else:
        status = "Fail"
    
    # Responsibility 3: Displaying output
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Status: {status}")

# Run the function
process_student()

def get_student_data():
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    return name, score

def determine_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

def display_results(name, score, status):
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Status: {status}")

# Use them together
student_name, student_score = get_student_data()
student_status = determine_status(student_score)
display_results(student_name, student_score, student_status)

def calculate_allowances():
    transport = 200.00
    meal = 150.00
    return transport + meal

def calculate_overtime(base_salary, overtime_hours):
    hourly_rate = base_salary / 160  # Assuming 160 working hours per month
    overtime_rate = hourly_rate * 1.5  # 1.5x for overtime
    return overtime_hours * overtime_rate

def calculate_epf(gross_salary):
    return gross_salary * 0.11

def calculate_socso(gross_salary):
    return gross_salary * 0.02

def calculate_net_salary(base_salary, overtime_hours):
    # Step 1: Calculate gross salary
    allowances = calculate_allowances()
    overtime = calculate_overtime(base_salary, overtime_hours)
    gross = base_salary + allowances + overtime
    
    # Step 2: Calculate deductions
    epf = calculate_epf(gross)
    socso = calculate_socso(gross)
    
    # Step 3: Calculate net
    net = gross - epf - socso
    return net

# Use it
salary = calculate_net_salary(5000, 10)
print(f"Net salary: RM{salary:.2f}")'''