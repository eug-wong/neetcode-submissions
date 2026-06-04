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
        
        dummy = ListNode(0, head)
        cur = dummy
        prev = None
        for _ in range(length - n + 1):
            prev = cur
            cur = cur.next

        if cur and prev:
            prev.next = cur.next

        return dummy.next