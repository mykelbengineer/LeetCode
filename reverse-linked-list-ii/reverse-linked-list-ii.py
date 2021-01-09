# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head or m == n: return head
        
        prev = dummy = ListNode(None)
        dummy.next = head
        curr = head
        
        for _ in range(m-1):
            prev = prev.next
            curr = curr.next
            
        for _ in range(n-m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
            
        
        return dummy.next
  
        
        
