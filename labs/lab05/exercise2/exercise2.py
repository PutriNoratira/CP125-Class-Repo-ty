
def find_largest_drop(readings):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    max_drop = 0.0
    for i in range (1, len(readings)):
        prev_temp = readings[i-1]
        cur_temp = readings[i]

        if cur_temp < prev_temp:
            current_drop = prev_temp - cur_temp

            if current_drop > max_drop:
                max_drop = current_drop

    return max_drop

# Test
readings = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(readings)
print(f"Largest Drop: {result}")  # Expected: 3.5
