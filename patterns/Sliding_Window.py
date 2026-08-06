def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        # Add the current element to the window sum
        window_sum += arr[window_end]

        # Once we reach the required window size k, we start sliding it
        if window_end >= k - 1:
            # Update the maximum sum achieved so far
            max_sum = max(max_sum, window_sum)
            
            # Subtract the element going out from the start of the window
            window_sum -= arr[window_start]
            
            # Slide the window start one step forward
            window_start += 1

    return max_sum

# Testing the code based on the image elements
numbers = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k_size = 5

result = max_sub_array_of_size_k(k_size, numbers)
print(f"Maximum sum of a subarray of size {k_size}: {result}")
# Explanation: The largest window of 5 elements is [6, -1, 4, 1, 8] and its sum = 18