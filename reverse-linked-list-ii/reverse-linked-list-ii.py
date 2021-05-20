# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = dummy = ListNode(None)
        dummy.next = curr = head
        
        for i in range(m-1):
            curr = curr.next
            prev = prev.next
            
            
        for i in range(n-m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
            
        return dummy.next

        
        