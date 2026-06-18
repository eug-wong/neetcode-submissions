# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # thing to notice
        # the LCA is going to be the node where p and q are no longer under same subtree
        def dfs(root):
            nonlocal p
            nonlocal q
            if not root or not p or not q:
                return None
            
            if (max(p.val, q.val) < root.val):
                return dfs(root.left)
            
            elif (min(p.val, q.val) > root.val):
                return dfs(root.right)
            
            else:
                return root

        return dfs(root)
            
