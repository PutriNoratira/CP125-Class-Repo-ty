# Method 1: Literal
menu = {"coffee": 5.00, "tea": 3.50}

# Method 2: Empty and add
menu = {}
menu["coffee"] = 5.00

# Method 3: dict() constructor
menu = dict(coffee=5.00, tea=3.50)

menu = {"coffee": 5.00}

price = menu.get("juice", 0.00)   # Returns 0.00 if not found — no crash

print (price)

menu["coffee"] = 6.00         # Update existing
menu["latte"] = 7.50          # Add new

# Batch update
menu.update({"tea": 4.00, "juice": 3.00})

del menu["tea"]               # Remove (KeyError if missing)
removed = menu.pop("latte")   # Remove and capture the value
menu.clear()                  # Remove everything