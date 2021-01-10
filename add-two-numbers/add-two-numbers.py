# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cur = dummyNode = ListNode(None)
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            cur_val = v1 + v2 + carry
            
            carry, cur_val = divmod(cur_val, 10)
            
            cur.next = ListNode(cur_val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        
        return dummyNode.next
                
                
        
        
            
