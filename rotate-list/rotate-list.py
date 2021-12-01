# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        
        old_head = head
        n = 1
        
        while old_head.next:
            old_head = old_head.next
            n += 1
            
        old_head.next = head
        tail = head
        
        for _ in range(n-k%n-1):
            tail = tail.next
            
        new_head = tail.next
        tail.next = None
        
        return new_head
        
        
        