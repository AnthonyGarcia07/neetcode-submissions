# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        # returns height
        def height(root):
            if not root:
                return 0

            # recursively returns the height of the subtrees
            left_height = height(root.left)
            right_height = height(root.right)

            # checks if the tree is balanced
            if abs(left_height - right_height) > 1:
                self.balanced = False
                return 0

            # returns the height to its parent
            return 1 + max(left_height, right_height)
            
        height(root)
        return self.balanced