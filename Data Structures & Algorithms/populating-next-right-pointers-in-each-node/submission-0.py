"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])

        while q:
            t = len(q)
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    if q and i < t - 1:
                        cur.next = q[0]
                    else:
                        cur.next = None

                    q.append(cur.left)
                    q.append(cur.right)
        
        return root
                