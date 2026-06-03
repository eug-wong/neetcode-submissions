# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -42
        count = k
        def dfs(root):
            nonlocal count
            nonlocal res
            if root:
                dfs(root.left)
                count -= 1
                if count == 0:
                    res = root.val
                    return
                dfs(root.right)
        
            return
        
        dfs(root)
        return res

                