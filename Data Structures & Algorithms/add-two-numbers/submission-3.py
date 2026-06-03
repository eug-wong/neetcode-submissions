# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 321 ->   123
        # 7654 -> 4567
        # 3
        # 4
        # res = 7975
        # 9999999
        #    9999
        # 99989991

        # 1. offset longer linked list by the difference
        # once offset is done, add and keep track of carry overs
        # return longer linked list/whichever is modified
        length1, length2 = 0, 0
        cur = l1
        while cur:
            length1 += 1
            cur = cur.next
        cur = l2
        while cur:
            length2 += 1
            cur = cur.next
        
        if length1 >= length2:
            longer = l1
            shorter = l2
        else:
            longer = l2
            shorter = l1
        
        res = longer
        carryover = 0
        prev = None
        while shorter:
            digit_sum = shorter.val + longer.val + carryover
            carryover = digit_sum // 10
            longer.val = digit_sum % 10
            prev = longer
            
            shorter = shorter.next
            longer = longer.next
        
        while longer and carryover:
            longer.val += 1 
            carryover = longer.val // 10
            longer.val = longer.val % 10
            prev = longer
            longer = longer.next
        
        if prev and carryover:
            prev.next = ListNode(1, None)

        return res

    
        
        