# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        de = deque()
        result = []
        de.append(root)

        while de:
            temp = []

            # popping
            for _ in range(len(de)):
                node = de.popleft()

                # repopulate queue with children
                if node:
                    temp.append(node.val)
                    de.append(node.left)
                    de.append(node.right)
            
            if temp:
                result.append(temp)
            
        return result
            

