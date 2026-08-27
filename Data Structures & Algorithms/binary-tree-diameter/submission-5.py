# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            # basecase
            if not node:
                return 0
            
            # get the heights of both subtrees first
            left = dfs(node.left)
            right = dfs(node.right)

            # diameter is the sum of the heights from the both subtrees
            diameter = max(diameter, left + right)

            # returning the height of both subtrees
            return 1 + max(left, right)
        
        dfs(root)

        return diameter
        
        