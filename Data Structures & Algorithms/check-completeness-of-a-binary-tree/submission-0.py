# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        layers = []
        while q:
            layer = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                layer.append(cur.val if cur else None)
            layers.append(layer)
        
        layers = layers[:-1]
        for layer in layers[: -1]:
            if layer.count(None) > 0:
                return False
        
        Noned = False
        for v in layers[-1]:
            if v and Noned:
                return False
            
            if not v:
                Noned = True
            
        return True
                