# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # returns height
        def dfs(curr):
            # base case for recursion
            if not curr:
                return 0

            # recursively gets the height of the left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            # stores the largest diameter
            self.res = max(self.res, left + right)

            # returns the height
            return 1 + max(left, right)

        dfs(root)
        return self.res

