# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return
        
        marker1 = marker2 = head
        
        while marker1 and marker1.next:
            marker2 = marker2.next
            marker1 = marker1.next.next
            
            if marker1 == marker2:
                break
                
        else:
            return None
        
        while head != marker1:
            head = head.next
            marker1 = marker1.next
            
        
        return head