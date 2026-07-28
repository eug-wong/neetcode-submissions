# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        layers = []
        q = deque([root])
        while q:
            l = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    l.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            layers.append(l)
        
        for i in range(len(layers)):
            if i % 2 == 1:
                layers[i] = layers[i][::-1]

        return layers[:-1]