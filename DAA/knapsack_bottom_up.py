def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: include the current item
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: exclude the current item
                exclude_item = dp[i - 1][w]
                # Take the maximum of including or excluding the item
                dp[i][w] = max(include_item, exclude_item)
            else:
                # If the item cannot be included, just carry forward the value
                dp[i][w] = dp[i - 1][w]
    
    # The bottom-right cell of the table contains the result
    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

result = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", result)
