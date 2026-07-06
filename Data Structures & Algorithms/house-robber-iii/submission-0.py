# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(root, can_rob):
            if not root:
                return 0
            
            # custom objects are hashable in python
            if (root, can_rob) in memo:
                return memo[(root, can_rob)]

            res = 0
            # 1 rob current house, flag that we cant rob next
            if can_rob:
                res = max(res, dfs(root.left, False) + dfs(root.right, False) + root.val)
            # 2 pass, flag we can rob next
            res = max(res, dfs(root.left, True) + dfs(root.right, True))

            memo[(root, can_rob)] = max(memo.get((root, can_rob), 0), res)
            return memo[(root, can_rob)]
        
        return dfs(root, True)