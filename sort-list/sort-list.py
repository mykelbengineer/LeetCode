# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
            
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.mergeList(left, right)
        
    
    
    def getMid(self,node):
        
        slow = fast = node
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
            
        slow.next = None
        
        return mid
    
    
    def mergeList(self, node1, node2):
        
        dummy = tail = ListNode(None)
        
        while node1 and node2:
            if node1.val < node2.val:
                tail.next, tail, node1 = node1, node1, node1.next
            else:
                tail.next, tail, node2 = node2, node2, node2.next
                
        tail.next = node1 or node2
        
        return dummy.next