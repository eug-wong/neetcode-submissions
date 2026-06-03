# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if current node is between p and q return it
        # if node is greater than both, search left
        # if ndoe is less than both, search right
        # if none, return
        t1, t2 = p.val, q.val
        p = min(t1, t2)
        q = max(t1, t2)

        lca = root
        def dfs(root, p, q):
            nonlocal lca
            if not root:
                return
            
            if p <= root.val <= q:
                lca = root
                return
            elif root.val > q:
                dfs(root.left, p, q)
            elif root.val < p:
                dfs(root.right, p, q)
            
            return
        
        dfs(root, p, q)
        return lca