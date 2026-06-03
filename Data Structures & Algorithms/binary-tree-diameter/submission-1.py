# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # what is the diameter of any subtree?
        
        max_diameter = 0
        def dfs(root) -> int:
            nonlocal max_diameter
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            max_diameter = max(max_diameter, l + r)
            return max(l, r) + 1
        
        dfs(root)
        
        return max_diameter