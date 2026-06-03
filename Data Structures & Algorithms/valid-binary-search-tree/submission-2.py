# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # when visiting left, update upper bound to cur val
        # when visiting right, update lower bound to cur val
        l = float('-inf')
        u = float('inf')
        valid = True
        def dfs(root, l, u):
            nonlocal valid
            if not root:
                return
            
            if l < root.val < u:
                dfs(root.left, l, root.val)
                dfs(root.right, root.val, u)
            else:
                valid = False
            
            return
        
        dfs(root, l, u)
        
        return valid