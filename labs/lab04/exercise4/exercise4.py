def analyze_performance(lap_times):
    total_lap = len(lap_times)
    half_lap = (total_lap + 1) // 2

    first_half = lap_times[:half_lap]
    second_half = lap_times[half_lap:]

    avg_1 = sum(first_half) / len(first_half)
    avg_2 = sum(second_half) / len(second_half)

    return avg_2 > avg_1

# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
