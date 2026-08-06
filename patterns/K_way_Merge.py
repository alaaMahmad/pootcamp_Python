import heapq

def merge_k_sorted_lists(lists):
    min_heap = []
    result = []

    # 1. Standard iteration using range(len(lists))
    for i in range(len(lists)):
        current_list = lists[i]  # List number i
        
        # Ensure the list is not empty
        if len(current_list) > 0:
            first_element = current_list[0] # The first element
            # Push: (value, list index i, element index inside the list which is 0)
            heapq.heappush(min_heap, (first_element, i, 0))

    # 2. Extraction and tracking process
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)

        # If there is a next element in the same list
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))

    return result