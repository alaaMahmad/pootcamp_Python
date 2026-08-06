def merge_intervals(intervals):
    if not intervals:
        return []

    # 1. Sort intervals based on the start of each interval [start, end]
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # 2. Check for overlap: if current start is less than or equal to previous end
        if current[0] <= last_merged[1]:
            # Merge intervals by updating the previous end to the maximum of both ends
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add current interval as is
            merged.append(current)

    return merged

# Testing the code
intervals_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals_list)

print(f"Merged Intervals: {result}")
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into [1,6]