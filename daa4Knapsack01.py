def knapsack_01(items, capacity):
    n = len(items)
    
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        item_id, value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:

                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:

                dp[i][w] = dp[i - 1][w]


    w = capacity
    knapsack_contents = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_id, value, weight = items[i - 1]
            knapsack_contents.append(item_id)
            w -= weight

    max_value = dp[n][capacity]
    return max_value, knapsack_contents[::-1]

items = [
    ('item1', 10, 10),
    ('item2', 20, 20),
    ('item3', 30, 30),
    ('item4', 40, 40),
    ('item5', 50, 80),
    ('item6', 60, 80)
]
capacity = 200
max_value, knapsack_contents = knapsack_01(items, capacity)
print("Maximum value in knapsack:", max_value)
print("Items in knapsack:", knapsack_contents)
