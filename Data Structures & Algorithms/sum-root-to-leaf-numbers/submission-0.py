# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # just a dfs prob
        # if we dont wanna keep track of var, we pass some total, multiple by 10 on the way up?
        # one way is just find height of tree first
        res = 0
        def dfs(root, cur):
            nonlocal res
            cur = cur + str(root.val)
            if root.left:
                dfs(root.left, cur)
            
            if root.right:
                dfs(root.right, cur)
            
            if not root.left and not root.right:
                res += int(cur)
            return
        
        dfs(root, "")
        return res
            
            
