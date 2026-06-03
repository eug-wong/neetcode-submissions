# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfway point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is halfway point
        # from slow onwards, we want to reverse the linked list
        # then merge list1 with list2
        list2 = slow.next
        slow.next = None
        cur = list2
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # list2 is head of second half reversed
        # list1 is head of first half
        list1 = head
        list2 = prev

        # now merge the two
        while list2:
            temp1, temp2 = list1.next, list2.next

            list1.next = list2
            list2.next = temp1

            list1, list2 = temp1, temp2

        return None