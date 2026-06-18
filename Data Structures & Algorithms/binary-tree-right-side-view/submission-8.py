# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        q = deque([root])
        while q:
            t = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    t.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if t:
                levels.append(t)
        
        res = []
        for level in levels:
            res.append(level[-1])
        
        return res