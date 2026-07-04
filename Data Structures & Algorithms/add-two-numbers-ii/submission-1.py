# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        cur = l1
        while cur:
            n1.append(cur.val)
            cur = cur.next
        
        cur = l2
        while cur:
            n2.append(cur.val)
            cur = cur.next
        
        len1, len2 = len(n1), len(n2)
        if len1 > len2:
            n2 = [0] * (len1 - len2) + n2
        else:
            n1 = [0] * (len2 - len1) + n1
        
        res = [0] * len(n1)
        carry = 0
        for i in range(len(n1) - 1, -1, -1):
            t = carry + n1[i] + n2[i]
            res[i] = t % 10
            carry = t // 10
        
        dummy = ListNode(carry, None)
        prev = dummy
        for i in range(len(res)):
            prev.next = ListNode(res[i], None)
            prev = prev.next

        return dummy if dummy.val else dummy.next