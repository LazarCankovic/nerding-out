# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # basecase
        if not root:
            return None

        # swap the children        
        root.left, root.right = root.right, root.left

        # keep swapping, until there is no more children so it goes to the basecase
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root