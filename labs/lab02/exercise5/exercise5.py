def is_valid_triangle (a, b, c):
    condition_1 = (a + b) > c
    condition_2 = (a + c) > b
    condition_3 = (b + c) > a

    return condition_1 and condition_2 and condition_3