'''
    My name is Tira.
    This program is written to sort, sum and find mx value of 5 
    numbers that are inserted by the user in ascending order. 
    I will be using list for keeping all the numbers inserted 
    by the user. Only then I'll be using built-in function 
    to sort, sum and find the max value
'''

def number_modifier(numbers):
    '''
    This function is to sort. calculate sum and find the
    highest value based on the number inserted by the user.
    '''
    numbers.sort()
    print (f"Numbers in ascending order: {numbers}")

    sum_numbers = sum(numbers)
    print (f"Sum of all numbers: {sum_numbers}")

    max_numbers = max(numbers)
    print (f"Largest number: {max_numbers}")

def number_input():
    '''
    This function is for the user to insert their 5 numbers.
    By using counter-controlled loop, it will ensure that the
    user only insert 5 numbers then it will process the numbers.
    '''
    numbers = []

    for i in range (1,6):
        number = int(input(f"Enter number {i}:"))
        numbers.append (number)
    
    number_modifier(numbers)

number_input()