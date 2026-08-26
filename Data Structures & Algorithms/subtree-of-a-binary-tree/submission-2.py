# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # basecases:
        # if subtree is None => automatic true
        if not subRoot:
            return True
        # if tree is None and subtree is not => automatic false
        if not root:
            return False
        # if the threes are the same, meaning compare the values => true
        if self.isSame(root, subRoot):
           return True
            
        # check the left/right side of the tree so that we find the subtree
        # within either side of the tree
        checkin_left = self.isSubtree(root.left, subRoot)
        checkin_right = self.isSubtree(root.right, subRoot)
        return checkin_left or checkin_right
    

    def isSame(self, p, q) -> bool:
        # basecases
        # first check if both null
        if not p and not q:
            return True
        # if one is null
        if not p or not q:
            return False
        # check the actual values
        if p.val != q.val:
            return False
        
        # go throgh all the children to do the comparisons
        left_vals = self.isSame(p.left, q.left)
        right_vals = self.isSame(p.right, q.right)
        
        # since both left and right have to be the same we use AND
        return left_vals and right_vals
