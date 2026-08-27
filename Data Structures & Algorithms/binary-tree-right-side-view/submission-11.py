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
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            levels.append(t)

        return [level[-1] for level in levels] if levels[0] else []
                
