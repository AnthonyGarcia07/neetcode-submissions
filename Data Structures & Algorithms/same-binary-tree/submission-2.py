# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both trees are NULL, return True
        if not p and not q:
            return True

        # if one tree is null return False
        # or the val at the nodes are not equal also return False
        if not p or not q or p.val != q.val:
            return False

        # returns True if both trees are equal
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
