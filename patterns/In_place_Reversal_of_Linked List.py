class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None      # Previous pointer (starts at None because the original head will become the last node)
    current = head   # Current pointer (starts at head)

    while current is not None:
        next_node = current.next  # 1. Save the next node so we don't lose it
        current.next = prev       # 2. Reverse the direction (current node now points to previous)
        prev = current            # 3. Move the previous pointer one step forward
        current = next_node       # 4. Move the current pointer one step forward

    return prev  # prev becomes the new head of the reversed list

# --- Helper function to print the list ---
def print_list(head):
    values = []
    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(values))

# Testing the code: creating list 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original List:")
print_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed List:")
print_list(reversed_head)

# Output:
# Original List:
# 1 -> 2 -> 3 -> 4
# Reversed List:
# 4 -> 3 -> 2 -> 1