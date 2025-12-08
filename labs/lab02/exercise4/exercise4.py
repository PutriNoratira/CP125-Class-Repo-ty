# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
    low_rate = 2.00
    high_rate = 5.00

    vehicle_type = vehicle_type.lower()

    if vehicle_type == "electric":
        rate = low_rate
        return low_rate
    elif vehicle_type == "hybrid":
        if hour_24 <= 6 or hour_24 >= 22:
            rate = low_rate
            return rate
        else:
            rate = high_rate
            return rate
    else:
        rate = high_rate
        return rate

# Test your code here
print ("Testing Dynamic Parking Rate...")