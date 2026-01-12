
def was_backward_detected(waypoints):
    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """
    for i in range (1, len(waypoints)):
        prev_x, prev_y, prev_z = waypoints[i-1]
        cur_x, cur_y, cur_z = waypoints[i]

        if (cur_x < prev_x) or (cur_y < prev_y):
            return True
    return False

# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
