def find_momentum_days(prices):
    momentum_indices = []

    for i in range (2, len(prices)):
        current_increase = prices[i] - prices [i-1]
        before_increase = prices [i-1] - prices [i-2]

        if (current_increase > 0) and (current_increase > before_increase):
            momentum_indices.append(i)
    
    return momentum_indices

# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]