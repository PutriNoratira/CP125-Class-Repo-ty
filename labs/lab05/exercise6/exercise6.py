
def find_slow_endpoints(api_calls, threshold):
    successful_calls = []
    for call in api_calls:
        if call[2] == 200:
            successful_calls.append(call)
    
    unique_names = set()
    for call in successful_calls:
        unique_names.add(call[0])
    
    slow_endpoints = []
    for name in unique_names:
            times = []
            for call in successful_calls:
                 if call[0] == name:
                      times.append(call[1])

            if len(times) >= 2:
                average = sum(times) / len(times)
                if average > threshold:
                    slow_endpoints.append(name)

    slow_endpoints.sort()
    return slow_endpoints

api_calls = [
    ("/login", 45, 200), 
    ("/login", 120, 200), 
    ("/data", 80, 200),
    ("/login", 50, 500),
    ("/data", 95, 200), 
    ("/search", 30, 200),
    ("/health", 150, 200)
]

result = find_slow_endpoints(api_calls, 70)
print(f"Slow endpoints: {result}")
