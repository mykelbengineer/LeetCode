# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(list1, list2):
            tail = dummy = ListNode(None)
            
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                    
                else:
                    tail.next = list2
                    list2 = list2.next
                    
                tail = tail.next
            
            if list1:
                tail.next = list1
                
            if list2:
                tail.next = list2
                
            
            return dummy.next
        
        
        return merge(l1,l2)