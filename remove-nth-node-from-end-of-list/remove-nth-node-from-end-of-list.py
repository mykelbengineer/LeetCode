# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        count = 0
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy
        
        while fast.next:
            fast = fast.next
            count += 1
            
        for _ in range(count - n):
            slow = slow.next
            
        if slow.next.next:
            slow.next = slow.next.next
        
        else:
            slow.next = None
            
        return dummy.next
