# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, ub):
            if not root:
                return 0
            
            res = 0
            if root.val >= ub:
                res += 1
            
            ub = max(root.val, ub)
            res += dfs(root.left, ub) + dfs(root.right, ub)

            return res
        
        return dfs(root, float('-inf'))

