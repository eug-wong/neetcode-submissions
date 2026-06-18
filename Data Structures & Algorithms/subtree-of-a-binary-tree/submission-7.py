# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        def dfs(root, subRoot):
            nonlocal res
            if not root and not subRoot:
                res = res or isSame(root, subRoot)
                return
            
            if not root:
                return
            
            if root and subRoot and root.val == subRoot.val:
                res = res or isSame(root, subRoot)
            
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
            return
        
        res = False
        dfs(root, subRoot)
        return res
