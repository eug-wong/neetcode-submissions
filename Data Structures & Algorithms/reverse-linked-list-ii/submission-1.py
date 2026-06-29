# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pprev = dummy
        cur = head
        for _ in range(left - 1):
            pprev = cur
            cur = cur.next
        
        prev = pprev
        for _ in range(right - left + 1):
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        
        if pprev:
            pprev.next.next = cur
            pprev.next = prev
            
        return dummy.next