# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2
        
        head = None
        curr = None
        left = list1
        right = list2
        
        if right.val >= left.val:
            head = left
            curr = head
            left = left.next
        else:
            head = right
            curr = head
            right = right.next

        while left is not None and right is not None:
            if right.val >= left.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next



        if left is not None:
            curr.next = left
        elif right is not None:
            curr.next = right
        
        return head