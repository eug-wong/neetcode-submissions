# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # some dfs
        # at every node, the depth of that subtree is max(l, r) + 1
        # so we return an integer upwards everytime we reach a new node recursively

        def dfs(root) -> int:
            if not root:
                return 0
            
            return max(dfs(root.left), dfs(root.right)) + 1
        
        return dfs(root)
