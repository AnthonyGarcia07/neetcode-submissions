# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subtree is a subtree of any tree
        if not subRoot:
            return True
        
        # A non-empty subtree cannot exist in an empty tree
        if not root:
            return False

        # Check if the trees starting at the current nodes are identical
        if self.sameTree(root, subRoot):
            return True

        # Search for a match in either the left or right subtree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        # Both nodes are empty, so they match
        if not root and not subRoot:
            return True

        # Different structure or node values means the trees don't match
        if not root or not subRoot or root.val != subRoot.val:
            return False

        # Both left and right subtrees must be identical
        return (self.sameTree(root.left, subRoot.left) and 
                self.sameTree(root.right, subRoot.right))