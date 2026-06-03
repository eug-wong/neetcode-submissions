# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = True

        def dfs(p, q):
            nonlocal isSame
            if not p and not q:
                return

            if not p and q:
                isSame = False
                return

            if not q and p:
                isSame = False
                return

            if p.val != q.val:
                isSame = False
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        
        dfs(p, q)

        return isSame