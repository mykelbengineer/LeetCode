# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2 : return None
        
        curr = dummy = ListNode(None)
        carry = 0
        
        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            
            total = val_1 + val_2 + carry
            carry, total = divmod(total, 10)
            
            curr.next = ListNode(total)
            curr = curr.next
            
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
        