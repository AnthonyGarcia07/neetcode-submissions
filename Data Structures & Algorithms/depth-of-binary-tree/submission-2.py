# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        # Checks the max depth for the left subtree and then right subtree
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        # returns the max between those two subtrees
        return max(left, right)