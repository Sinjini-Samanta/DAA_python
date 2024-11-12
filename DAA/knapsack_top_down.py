def knapsack(weights, values, capacity):
    n = len(weights)
    
    # Create a memoization table to store results of subproblems
    memo = {}

    # Helper function with memoization
    def dp(i, w):
        # If no items left or capacity is 0, return 0
        if i == n or w == 0:
            return 0
        
        # If the result is already computed, return it from memo
        if (i, w) in memo:
            return memo[(i, w)]
        
        # If the current item's weight is more than the remaining capacity, skip it
        if weights[i] > w:
            memo[(i, w)] = dp(i + 1, w)  # move to the next item without including this one
        else:
            # Option 1: include the item
            include_item = values[i] + dp(i + 1, w - weights[i])
            # Option 2: don't include the item
            exclude_item = dp(i + 1, w)
            # Take the maximum of including or excluding the item
            memo[(i, w)] = max(include_item, exclude_item)
        
        return memo[(i, w)]
    
    # Start the recursion from the 0th item and given capacity
    return dp(0, capacity)

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

result = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", result)
