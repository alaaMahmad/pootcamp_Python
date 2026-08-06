class Solution:
    def solve_knapsack(self, weights, profits, capacity):
        n = len(weights)
        # dp[i][c] represents the max profit with first i items and capacity c
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # Build DP table in bottom-up manner
        for i in range(1, n + 1):
            current_weight = weights[i - 1]
            current_profit = profits[i - 1]
            
            for c in range(1, capacity + 1):
                # Option 1: Do not include current item
                exclude_item = dp[i - 1][c]
                
                # Option 2: Include current item (if capacity allows)
                include_item = 0
                if current_weight <= c:
                    include_item = current_profit + dp[i - 1][c - current_weight]
                
                # Store the max profit choice
                dp[i][c] = max(exclude_item, include_item)

        return dp[n][capacity]


# ==========================================
#      Execution Example with Prints
# ==========================================

solution = Solution()
item_weights = [1, 2, 3]
item_profits = [10, 15, 40]
knapsack_capacity = 6

print("--- Executing 0/1 Knapsack (Dynamic Programming) ---")
print(f"Weights:  {item_weights}")
print(f"Profits:  {item_profits}")
print(f"Capacity: {knapsack_capacity}")

max_profit = solution.solve_knapsack(item_weights, item_profits, knapsack_capacity)

print("\n--- Execution Result ---")
print(f"Maximum Profit Achievable: {max_profit}")