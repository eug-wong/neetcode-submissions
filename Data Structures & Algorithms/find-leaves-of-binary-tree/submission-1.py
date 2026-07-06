# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            h = max(dfs(root.left), dfs(root.right)) + 1
            if h - 1 == len(res):
                res.append([])
            
            res[h - 1].append(root.val)
            return h
        
        dfs(root)
        return res