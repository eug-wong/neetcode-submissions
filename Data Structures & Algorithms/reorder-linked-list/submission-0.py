# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5]
        #  0 -> 5 -> 1 -> 4 -> 2 -> 3
        # 0 1 2       5 4 3
        # 0 5 1 4 2 3
        
        # 1. find list 2
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next

        # 2. reverse list 2
        prev = slow.next = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        # 3. zip it up
        f, s = head, prev
        while s:
            tmp1, tmp2 = f.next, s.next
            f.next = s
            s.next = tmp1
            f, s = tmp1, tmp2
        


        