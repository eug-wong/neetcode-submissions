# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        multiple = 1
        if l1 and l1.val == 0 and l2 and l2.val == 0:
            return l1
        while l1:
            num1 += l1.val * multiple
            multiple *= 10
            l1 = l1.next
        
        multiple = 1
        while l2:
            num2 += l2.val * multiple
            multiple *= 10
            l2 = l2.next
        
        num = str(num1 + num2)

        # generate linked list
        dummy = ListNode()
        head = dummy
        while int(num) > 0:
            newNode = ListNode(int(num[-1]))
            head.next = newNode
            head = head.next
            num = str(int(int(num)/10))
        
        return dummy.next
        
        