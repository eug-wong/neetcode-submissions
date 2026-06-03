# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        start = subRoot.val
        isSubtree = False

        def dfs(root, subRoot):
            nonlocal isSubtree
            nonlocal start
            if not root:
                return

            if root.val == start:
                isSubtree = dfs_check(root, subRoot)
                if isSubtree:
                    return
                
            
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
        
        def dfs_check(root, subRoot):
            # check if two trees are identical
            if not root and not subRoot:
                return True
            elif root and subRoot and root.val == subRoot.val:
                return dfs_check(root.left, subRoot.left) and dfs_check(root.right, subRoot.right)
            else:
                return False
            
        
        dfs(root, subRoot)
        return isSubtree
