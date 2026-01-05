def has_warming_trend(temps):
    for i in range (len(temps) - 2):
        if temps[i+1] > temps[i]:
            if temps[i+2] > temps[i]:
                return True
    return False