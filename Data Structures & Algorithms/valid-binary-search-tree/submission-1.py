# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = float('-inf')
        u = float('inf')

        def dfs(root, l, u):
            if not root:
                return True

            if not (l < root.val < u):
                return False
            
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, u)
        
        return dfs(root, l, u)