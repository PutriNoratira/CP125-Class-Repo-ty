def has_adjacent_seats(seats):
    for i in range (len(seats) - 1):
        if seats[i] == 0:
            if seats[i + 1] == 0:
                return True
    return False
