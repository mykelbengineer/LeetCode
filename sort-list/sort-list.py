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
        
        return self.mergeList(left,right)
        
        
    def getMid(self, linkedList):
        
        slow = fast = linkedList
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            
        mid = slow.next
        slow.next = None
        
        return mid
    
    
    def mergeList(self, list1, list2):
        
        tail = dummy = ListNode(None)
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        if list1: tail.next = list1
        if list2: tail.next = list2
            
        return dummy.next
        
        