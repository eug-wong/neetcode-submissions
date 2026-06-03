"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first make a copy of every node
        # then just iterate thru and link them together
        # we can map old nodes to new nodes?
        old_to_new = {}
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)
            old_to_new[cur] = new_node
            cur = cur.next
        
        # old to new w/o next or random
        # string it all together
        cur = head
        while cur:
            new_node = old_to_new[cur]
            if cur.next:
                new_node.next = old_to_new[cur.next]
            if cur.random:
                new_node.random = old_to_new[cur.random]
            cur = cur.next
        
        return old_to_new[head] if head else None
        





