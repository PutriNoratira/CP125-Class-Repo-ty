
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    if len(times) == 0:
        return []

    count = len(times)
    mean = sum(times) / count

    variance_sum = 0
    for x in times:
        difference = x - mean
        variance_sum += difference * difference

    variance = variance_sum / count
    std_dev = variance ** 0.5
    limit = mean + std_dev

    clean_list = []
    for y in times:
        if y <= limit:   # keep values <= mean + std
            clean_list.append(y)

    clean_list.sort()
    return clean_list

# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
