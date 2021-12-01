# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None  
        if not head.next : return head
        
        prev = dummy = ListNode(-1)
        dummy.next = head
        
        
        while head and head.next:
            
            firstNode = head
            secondNode = head.next
            
            
            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            
            prev = firstNode
            head = firstNode.next
            
        
        return dummy.next
            
            
        
        
        