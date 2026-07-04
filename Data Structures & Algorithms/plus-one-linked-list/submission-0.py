# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def recurse(cur):
            if not cur:
                return 1
            
            cur.val += recurse(cur.next)
            carry = cur.val // 10
            cur.val = cur.val % 10
            return carry
        
        carry = recurse(head)
        if carry:
            head = ListNode(carry, head)
        
        return head
