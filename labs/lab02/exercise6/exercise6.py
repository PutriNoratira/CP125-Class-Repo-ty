def is_leap_year(year):
    """
    Determines if a year is a leap year according to the Gregorian calendar.
    
    Rules:
    1. If divisible by 4 -> Yes
    2. BUT if divisible by 100 -> No
    3. UNLESS divisible by 400 -> Yes
    
    Parameters:
    year: Integer year value
    
    Returns:
    True if leap year, False otherwise
    """
    # TODO: Implement the leap year logic
    # Hint: Check divisibility in the correct order

    divisible_by_4 = (year % 4 == 0)
    divisible_by_100 = (year % 100 == 0)
    divisible_by_400 = (year % 400 == 0)

    is_leap = divisible_by_4 and (not divisible_by_100 or divisible_by_400)

    return is_leap