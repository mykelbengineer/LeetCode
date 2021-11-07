# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        
        slow = fast = dummy = ListNode(None)
        dummy.next = head
        
        for _ in range(n):
            fast = fast.next
            
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        
        return dummy.next
            
        