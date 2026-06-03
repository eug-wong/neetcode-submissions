# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def dfs(p, q):
            nonlocal same
            if not p and not q:
                return
            elif not p and q:
                same = False
                return
            elif not q and p:
                same = False
                return
            
            if p.val != q.val:
                same = False
                return 
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)
            return
        
        dfs(p, q)
        
        return same