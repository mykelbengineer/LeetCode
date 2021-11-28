# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        oddHead = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            oddHead.next = oddHead.next.next
            even.next = even.next.next
            
            even = even.next
            oddHead = oddHead.next
            
        oddHead.next = evenHead
        
        return head
        