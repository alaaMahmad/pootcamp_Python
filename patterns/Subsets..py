def find_subsets(nums):
    # Start with one empty subset inside the list
    subsets = [[]]
    
    for current_number in nums:
        # Calculate the number of current subsets to make copies of them
        n = len(subsets)
        for i in range(n):
            # Take a copy of the current subset and add the new number to it
            set_copy = list(subsets[i])
            set_copy.append(current_number)
            subsets.append(set_copy)
            
    return subsets

# Testing the code:
nums = [1, 3]
print(find_subsets(nums))
# Output: [[], [1], [3], [1, 3]]