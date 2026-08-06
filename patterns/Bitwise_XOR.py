def find_single_number(nums):
    x1 = 0
    # Apply the XOR operation across all elements in the list
    for num in nums:
        x1 ^= num  # Same as x1 = x1 ^ num
    
    return x1

# Testing the code:
arr = [1, 4, 2, 1, 3, 2, 3]
print(find_single_number(arr))  # Output: 4