"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        newList = dummy = Node(-1)
        old_new_map = {}
        curr = head
        
        while curr:
            newList.next = Node(curr.val)
            old_new_map[curr] = newList.next
            curr = curr.next
            newList = newList.next
            
        curr = head
        newHead = dummy.next
        
        while curr:
            if curr.random:
                newHead.random = old_new_map[curr.random]
                
            curr = curr.next
            newHead = newHead.next
            
        return dummy.next
            
        
        
        