def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_profit = 0.0
    knapsack_contents = []

    for item_id, profit, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            
            capacity -= weight
            total_profit += profit
            knapsack_contents.append((item_id, 1))
        else:

            fraction = round(capacity / weight , 2)
            total_profit += profit * fraction
            knapsack_contents.append((item_id, fraction))
            capacity = 0

    return total_profit, knapsack_contents

items = [
    ('item1', 60, 10), 
    ('item2', 100, 20),
    ('item3', 120, 30)
]
capacity = 50
total_profit, knapsack_contents = fractional_knapsack(items, capacity)
print("Maximum profit in knapsack:", total_profit)
print("Items in knapsack (item_id, fraction):", knapsack_contents)
