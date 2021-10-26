# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head: return None
        
        count = 0
        curr = dummy = ListNode(None)
        counter = dummy.next = head

        
        while counter:
            count += 1
            counter = counter.next
            
        num_to_remove = count - n
        
        while num_to_remove:
            curr = curr.next
            num_to_remove -= 1
            
            
        curr.next = curr.next.next
        
        return dummy.next