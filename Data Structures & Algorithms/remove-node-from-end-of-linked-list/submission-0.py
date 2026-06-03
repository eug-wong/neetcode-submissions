# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        to_remove = length - n
        cur = head
        prev = None
        if to_remove == 0:
            return head.next
        while cur:
            if to_remove == 0:
                prev.next = cur.next
                break
            else:
                prev = cur
                cur = cur.next
                to_remove -= 1
        
        return head