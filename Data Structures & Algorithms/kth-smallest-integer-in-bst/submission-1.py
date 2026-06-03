# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # just a dfs? keep track of k
        res = root.val
        def dfs(root):
            nonlocal res
            nonlocal k
            if not root:
                return
            
            # always go left first, to get min
            dfs(root.left)
            
            k -= 1
            if k == 0:
                res = root.val
                return
            
            dfs(root.right)
            
            return
        
        dfs(root)
        
        return res