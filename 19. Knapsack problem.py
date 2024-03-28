def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    knapsack = []
    for weight, value in items:
        if capacity >= weight:
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((capacity, fraction * value))
            total_value += fraction * value
            break
    return total_value, knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
total_value, knapsack = fractional_knapsack(weights, values, capacity)
print("Total value obtained:", total_value)
print("Items in the knapsack:")
for weight, value in knapsack:
    print("Weight:", weight, "Value:", value)