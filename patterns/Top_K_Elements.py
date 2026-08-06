import heapq

def find_top_k_numbers(nums, k):
    min_heap = []
    
    # 1. Push the first K elements into the Min-Heap
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
        
    # 2. Iterate through the remaining elements
    for i in range(k, len(nums)):
        # If the current element is larger than the smallest element in the Heap
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)      # Remove the smallest element
            heapq.heappush(min_heap, nums[i])  # Push the new element
            
    # The Heap now contains the largest K elements
    return min_heap

# Testing the code:
nums = [3, 1, 5, 12, 2, 11]
k = 3
print(find_top_k_numbers(nums, k))  # Output: [5, 11, 12]