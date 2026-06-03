# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # at each node, keep track of max seen so far
        # if node val is less than or equal to max, count += 1
        count = 0
        def dfs(root, maximum):
            nonlocal count
            if not root:
                return
            
            maximum = max(maximum, root.val)
            if maximum <= root.val:
                count += 1
            
            dfs(root.left, maximum)
            dfs(root.right, maximum)
            return
        
        dfs(root, float('-inf'))
        
        return count
            