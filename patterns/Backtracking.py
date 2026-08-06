class Solution:
    def subsets(self, nums):
        result = []
        path = []

        def backtrack(start_index):
            # Base Case: Every valid state along the recursion tree is a subset
            result.append(list(path))

            # Explore all options from start_index to the end of array
            for i in range(start_index, len(nums)):
                # 1. Choose: Add current number to option path
                path.append(nums[i])

                # 2. Explore: Move forward to next index
                backtrack(i + 1)

                # 3. Unchoose (Backtrack): Remove last choice to try other options
                path.pop()

        backtrack(0)
        return result


# ==========================================
# 🧪 Execution Example with Prints
# ==========================================

solution = Solution()
input_nums = [1, 2, 3]

print("--- Executing Backtracking for Subsets ---")
print(f"Input Array: {input_nums}")

output = solution.subsets(input_nums)

print("\n--- Final Generated Subsets ---")
print(f"Total Subsets Generated: {len(output)}")
print("Subsets Output:", output)