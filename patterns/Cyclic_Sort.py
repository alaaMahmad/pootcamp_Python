def find_missing_number(nums):
    i = 0
    n = len(nums)

    # 1. Apply Cyclic Sort
    while i < n:
        j = nums[i]  # The correct index where nums[i] should go
        
        # Swap numbers if the number is smaller than list size and not in its correct position
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # Pythonic swap operation
        else:
            i += 1

    # 2. Find the first index that does not match the stored value
    for i in range(n):
        if nums[i] != i:
            return i  # This index is the missing number

    return n  # If all numbers are in place, the missing number is n itself

# Testing the code
numbers = [4, 0, 3, 1] 
# The list has 4 elements and the range is from 0 to 4; the missing number is 2

result = find_missing_number(numbers)
print(f"The missing number is: {result}")
# Output: The missing number is: 2