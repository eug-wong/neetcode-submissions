# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        
        cur1 = prev
        cur2 = head
        res = 0
        while cur1:
            res = max(res, cur1.val + cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
    
        return res
