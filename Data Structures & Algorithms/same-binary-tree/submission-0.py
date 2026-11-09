# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # checks if both trees are empty, returns true
        if not p and not q:
            return True

        # checks if either tree is empty
        # or if the root values are not equal
        # returns false since both trees are not the same
        if not p or not q or p.val != q.val:
            return False


        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))