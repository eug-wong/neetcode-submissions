# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root, key):
            if not root:
                return root
            
            if root.val > key:
                root.left = dfs(root.left, key)
            elif root.val < key:
                root.right = dfs(root.right, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                
                cur = root.right
                while cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = dfs(root.right, root.val)
                
            return root
        
        return dfs(root, key)