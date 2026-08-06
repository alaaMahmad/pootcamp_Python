import heapq

class MedianFinder:
    def __init__(self):
        # max_heap holds the smaller half (stored as negative values)
        self.max_heap = [] 
        # min_heap holds the larger half
        self.min_heap = [] 

    def add_num(self, num: int) -> None:
        # 1. Insert the number into Max-Heap first, or based on its value
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # 2. Balancing: Ensure the size difference between the two heaps is at most one element
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Transfer the largest element from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            # Transfer the smallest element from min_heap to max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self) -> float:
        # If the total number of elements is odd, the median is the top element of max_heap
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        # If the total number of elements is even, the median is the average of both heap tops
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# Testing the code:
finder = MedianFinder()
finder.add_num(3)
finder.add_num(1)
print(f"Median: {finder.find_median()}")  # Output: 2.0 (Average of 1 and 3)

finder.add_num(5)
print(f"Median: {finder.find_median()}")  # Output: 3.0 (Median of 1, 3, 5)