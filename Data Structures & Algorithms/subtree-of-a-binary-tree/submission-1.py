# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case 1 - empty tree = always a subtree
        if not subRoot:
            return True
        
        # base case 2 - empty root = no subtree possible
        if not root:
            return False
        
        # checking if the trees are the same
        if self.isSameTree(root, subRoot):
            return True

        # keep looking in the subtrees of the root
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # helper to see if the values match from both trees
    def isSameTree(self, p, q):
        # if both null, it's fine
        if not p and not q:
            return True
        # if one is, but the other one is not false
        if not p or not q:
            return False
        # if the values are not identical false
        if p.val != q.val:
            return False
        # check for every single node
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        