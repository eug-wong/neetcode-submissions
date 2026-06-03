# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return False
        
        subtree = False
        def dfs(root, subRoot):
            nonlocal subtree
            if not root:
                return
            # print("testing: ", root.val, subRoot.val)
            if root.val == subRoot.val:
                # print("testing: ", root.val, subRoot.val)
                subtree = isSame(root, subRoot)
                if subtree:
                    return
            
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
            return
        
        dfs(root, subRoot)
        
        return subtree