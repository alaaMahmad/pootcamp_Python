# Definition of a Node structure in a Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    # Continue iterating as long as the fast pointer hasn't reached the end of the list
    while fast is not None and fast.next is not None:
        slow = slow.next          # Move one step
        fast = fast.next.next     # Move two steps

        # If both pointers meet, a cycle exists
        if slow == fast:
            return True

    return False  # If fast reaches None, there is no cycle

# ----- Testing the code -----
# Creating list nodes: 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

# Creating a cycle: connecting node 6 back to node 3
head.next.next.next.next.next.next = head.next.next

print(f"Has Cycle? {has_cycle(head)}") 
# Output: True