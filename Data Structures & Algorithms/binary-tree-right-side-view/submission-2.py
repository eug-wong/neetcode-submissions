# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        de = deque()
        de.append(root)
        res = []
        last = None

        # BFS
        while de:
            l = len(de)

            for _ in range(l):
                node = de.popleft()
                if node:
                    last = node

                if node:
                    de.append(node.left)
                    de.append(node.right)

            if last:
                res.append(last.val)
                last = None
        
        return res