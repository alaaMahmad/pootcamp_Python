def binary_search(arr, key):
    start, end = 0, len(arr) - 1

    # Determine if the array is sorted in ascending or descending order
    is_ascending = arr[start] < arr[end]

    while start <= end:
        # Calculate the middle element to prevent overflow
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid

        if is_ascending:  # Ascending order
            if key < arr[mid]:
                end = mid - 1   # Search the left half
            else:
                start = mid + 1  # Search the right half
        else:  # Descending order
            if key > arr[mid]:
                end = mid - 1   # Search the left half
            else:
                start = mid + 1  # Search the right half

    return -1  # Return -1 if the element is not found

# Testing the code:
print(binary_search([4, 6, 10], 10))        # Ascending -> Output: 2
print(binary_search([10, 6, 4], 10))        # Descending -> Output: 0