# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cur_max = root.val
        count = 0

        def dfs(root, cur_max):
            nonlocal count

            if root and root.val >= cur_max:
                count += 1
            
            if root:
                cur_max = max(cur_max, root.val)
                dfs(root.left, cur_max)
                dfs(root.right, cur_max)
            
            return
        
        dfs(root, cur_max)
        
        return count