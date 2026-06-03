# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        p_val = p.val
        q_val = q.val

        # is p less than q?
        # make sure p < q
        if p_val > q_val:
            temp = p_val
            p_val = q_val
            q_val = temp

        
        def dfs(root, p, q):
            nonlocal lca
            val = root.val
            print("val: ", val)

            print(p <= val, val <= q, p, q)

            if (p <= val) and (val <= q):
                lca = root
                print("lca updated: ", lca)
                return
            
            elif (val >= p) and (val >= q):
                print("going left: ", val)
                dfs(root.left, p, q)
            
            elif (val <= p) and (val <= q):
                print("going right: ", val)
                dfs(root.right, p, q)
            
            return
        
        dfs(root, p_val, q_val)
        return lca