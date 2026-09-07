"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
            
        headcpy = head
        newhead = newheadcpy = Node(head.val)
        seen: dict = {headcpy:newheadcpy}

        while headcpy:
            headcpy = headcpy.next
            if headcpy:
                newheadcpy.next = Node(headcpy.val)
                newheadcpy = newheadcpy.next
                seen[headcpy] = newheadcpy
        
        headcpy, newheadcpy = head, newhead
        while headcpy:
            if headcpy.random in seen:
                newheadcpy.random = seen[headcpy.random]
            newheadcpy = newheadcpy.next
            headcpy = headcpy.next
        
        return newhead
            