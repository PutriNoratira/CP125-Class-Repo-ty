def get_position(cars, car_number):
    for i in range (len(cars)):
        if cars[i] == car_number:
            return i

def has_overtaken(before, after, car1, car2):
    pos1_before = get_position(before, car1)
    pos2_before = get_position(before, car2)
    pos1_after = get_position(after, car1)
    pos2_after = get_position(after, car2)

    if (pos1_before > pos2_before) and (pos1_after < pos2_after):
        return True
    return False