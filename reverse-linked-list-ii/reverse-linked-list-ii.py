# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = dummy = ListNode(None)
        curr = dummy.next = head
        
        for i in range(m-1):
            curr = curr.next
            prev = prev.next

        for i in range(n-m):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
        
        