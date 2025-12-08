# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    # TODO: Implement this function
    # Return True if valid, False otherwise
    director = (name == "Director" and pin == 1122)
    security = (name == "Security" and pin == 9900)

    access = director or security

    return access

# Test your code here
print("Testing Secure Vault System...")
