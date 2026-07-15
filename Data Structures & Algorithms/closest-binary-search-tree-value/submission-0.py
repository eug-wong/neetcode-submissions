# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return
            
            if abs(res - target) > abs(root.val - target):
                res = root.val

            dfs(root.left)
            dfs(root.right)
            return
        
        dfs(root)
        return res