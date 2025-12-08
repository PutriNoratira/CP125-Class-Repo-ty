# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    tent_needed = math.ceil(participants/tent_capacity)
    total_tent_price = tent_needed * tent_price
    total_meal_price = meal_price * participants
    total_cost = total_tent_price + total_meal_price
    return total_cost

# Test your code here
print("Testing Camping Logistics...")
