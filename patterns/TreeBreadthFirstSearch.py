from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_level_order(root):
    result = []
    if not root:
        return result

    # We use deque as a Queue, which is faster and more efficient than regular lists
    queue = deque([root])

    while queue:
        level_size = len(queue) # Number of nodes in the current level
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft() # Pop node from the front of the queue
            current_level.append(current_node.val)

            # Add child nodes (left and right) to the queue for the next level
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level) # Append the entire level to the result

    return result

# Testing the code on a binary tree structure:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

print(traverse_level_order(root))
# Output: [[1], [2, 3], [4, 5, 6, 7]]