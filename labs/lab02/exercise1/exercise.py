# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    total_distance = one_way_km * 2
    total_litre = total_distance/km_per_liter
    total_price = total_litre * price_per_liter
    return total_price >= budget

# Test your code here
print("Testing Road Trip Budgeter...")
