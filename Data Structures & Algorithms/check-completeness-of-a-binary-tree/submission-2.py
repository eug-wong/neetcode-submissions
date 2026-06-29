# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seen_none = False
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    if seen_none:
                        return False
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    seen_none = True
            
        return True
                