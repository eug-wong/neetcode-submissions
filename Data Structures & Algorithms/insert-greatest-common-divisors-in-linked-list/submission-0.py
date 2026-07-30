# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
            if prev and cur:
                big, small = max(prev.val, cur.val), min(prev.val, cur.val)
                remainder = small
                while big % small != 0:
                    remainder = big % small
                    big = small
                    small = remainder
                new_node = ListNode(remainder, cur)
                prev.next = new_node

        return head
