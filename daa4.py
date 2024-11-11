def knapsack_dp(W, weights, values, n):
    # Initialize a DP table with all values set to 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Take maximum of including or excluding the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If item cannot be included, just carry forward the previous value
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value achievable with the given weight capacity
    return dp[n][W]

# Main function
if __name__ == "__main__":
    # Input number of items
    n = int(input("Enter the number of items: "))
    
    # Input weights and values of items
    weights = []
    values = []
    print("Enter the weight and value of each item:")
    for i in range(n):
        weight, value = map(int, input(f"Item {i + 1} weight and value: ").split())
        weights.append(weight)
        values.append(value)
    
    # Input capacity of knapsack
    W = int(input("Enter the capacity of the knapsack: "))

    # Calculate maximum value using knapsack DP function
    max_value = knapsack_dp(W, weights, values, n)
    print("Maximum value the thief can carry:", max_value)
