def pair_with_target_sum(arr, target):
    # Set the left pointer at the start and the right pointer at the end
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        # If we find the target sum
        if current_sum == target:
            return [left, right] # Return the element indices
        
        # If the sum is smaller than target, move the left pointer forward to increase the value
        if current_sum < target:
            left += 1
        # If the sum is larger than target, move the right pointer backward to decrease the value
        else:
            right -= 1
            
    return [-1, -1] # Return [-1, -1] if no pair satisfies the condition

# Testing the code
numbers = [1, 2, 3, 4, 6]
target_val = 6

result = pair_with_target_sum(numbers, target_val)
print(f"Indices of numbers that add up to {target_val}: {result}")
# Output: [1, 3] (because 2 + 4 = 6)