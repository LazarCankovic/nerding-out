# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # basecases
        # if both null = true
        if not p and not q:
            return True
        # if one of them null while the other is not = false
        if not p or not q:
            return False
        # if the values of those nodes are not the same = false
        if p.val != q.val:
            return False

        # now go through all the nodes on the left, then right
        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)

        return left_subtree and right_subtree