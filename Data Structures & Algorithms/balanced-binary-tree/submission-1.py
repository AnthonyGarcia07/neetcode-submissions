# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        # Returns height
        def height(root):
            if not root:
                return 0

            # Recursively call the heights for subtrees
            height_left = height(root.left)
            height_right = height(root.right)

            # Checks if the height at a specific node is balanced
            if abs(height_left - height_right) > 1:
                self.balanced = False
                return 0 

            # returns height to parent
            return 1 + max(height_left, height_right)

        height(root)
        return self.balanced