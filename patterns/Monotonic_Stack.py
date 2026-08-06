class Solution:
    def next_greater_element(self, nums):
        n = len(nums)
        result = [-1] * n  # Initialize result array with -1
        stack = []         # Monotonic Stack storing indices

        for i in range(n):
            current_val = nums[i]
            
            # Maintain monotonic decreasing property
            # While current element is greater than the stack top element
            while stack and nums[stack[-1]] < current_val:
                prev_index = stack.pop()
                result[prev_index] = current_val  # Found next greater element
                
            # Push current index onto stack
            stack.append(i)

        return result


# ==========================================
# 🧪 Execution Example with Prints
# ==========================================

solution = Solution()
input_array = [2, 1, 2, 4, 3]

print("--- Executing Monotonic Stack (Next Greater Element) ---")
print(f"Input Array: {input_array}")

output = solution.next_greater_element(input_array)

print("\n--- Next Greater Elements Result ---")
print(f"Original Array: {input_array}")
print(f"Result Array:   {output}")