# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        d = deque()
        if root:
            d.append(root)
        
        while d:
            n = len(d)
            row = []
            vals = []
            new = []
            for _ in range(n):
                row.append(d.popleft())
                vals.append(row[-1].val)
                if row[-1].left:
                    new.append(row[-1].left)
                if row[-1].right:
                    new.append(row[-1].right)
            res.append(vals)
            d += new
        
        return res
