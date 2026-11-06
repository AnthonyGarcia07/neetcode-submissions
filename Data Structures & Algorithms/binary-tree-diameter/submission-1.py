# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # Returns height
        def dfs(curr):
            if not curr:
                return 0
            
            # Recieves the height for the left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Returns the diameter
            self.res = max(self.res, left + right)
            
            # Returns the subtree's height to its parent
            return 1 + max(left, right)

        # passes the root into the function dfs
        dfs(root)
        return self.res
