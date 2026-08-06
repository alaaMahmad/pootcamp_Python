class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target_sum):
    # Base case: if the tree is empty
    if not root:
        return False

    # 1. If we reach a leaf node with no children
    if not root.left and not root.right:
        return root.val == target_sum

    # 2. Subtract from the sum and test left and right branches recursively
    remaining_sum = target_sum - root.val
    
    return (has_path_sum(root.left, remaining_sum) or 
            has_path_sum(root.right, remaining_sum))

# Testing the code on the following tree:
#        12
#       /  \
#      7    1
#     /    / \
#    9    10  5
#
# Is there a path with a sum of 23? (Yes: 12 -> 1 -> 10 = 23)

root = TreeNode(12)
root.left = TreeNode(7, TreeNode(9))
root.right = TreeNode(1, TreeNode(10), TreeNode(5))

print(has_path_sum(root, 23)) # Output: True (12 + 1 + 10 = 23)
print(has_path_sum(root, 16)) # Output: False