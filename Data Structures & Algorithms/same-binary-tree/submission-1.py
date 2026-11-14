# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both trees are NULL
        if not p and not q:
            return True
        
        # Checks if one tree is null or if the root values are not equal
        if not p or not q or p.val != q.val:
            return False

        # Checks if the left and right subtrees are identical
        # Returns True only if both comparisons return True
        return(self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))