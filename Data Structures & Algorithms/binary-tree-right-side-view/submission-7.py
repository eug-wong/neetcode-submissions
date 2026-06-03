# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]
        d = deque([root])

        while d:
            n = len(d)
            t = []
            for _ in range(n):
                node = d.popleft()
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
            if t:
                res.append(t[-1].val)
            d += t
            
        return res