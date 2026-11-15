# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subroot is null, returns true
        if not subRoot: 
            return True

        # if root is null, returns False
        if not root:
            return False

        # if both trees are the same, return true
        if self.isSameTree(root, subRoot):
            return True
        
        # search the left or right subtree for a match
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))


    # Helper function checking if the subtrees are the same
    def isSameTree(self, root, subRoot):
        # if both subtrees are null, return true
        if not root and not subRoot:
            return True

        # if one subtree is null, or the vals are not equal, return false
        if not root or not subRoot or root.val != subRoot.val:
            return False

        # if both return True, this means they are the same subtrees with the same structure
        return (self.isSameTree(root.left, subRoot.left) and
                self.isSameTree(root.right, subRoot.right))