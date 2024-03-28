def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)  # Sort items by value-to-weight ratio
    total_value = 0
    knapsack = []
    for weight, value in items:
        if capacity >= weight:
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((weight * fraction, value * fraction))
            total_value += value * fraction
            break
    return knapsack, total_value
items = [(2, 3), (3, 4), (4, 5), (5, 6)]
capacity = 5
optimal_knapsack, optimal_value = fractional_knapsack(items, capacity)
print("Optimal knapsack:", optimal_knapsack)
print("Optimal value:", optimal_value)