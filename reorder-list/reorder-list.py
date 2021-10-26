# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast = slow = dummy = ListNode
        dummy.next = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        l1 = dummy.next
        l2 = slow.next
        
        slow.next = None
        
        prev = None
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp
        
        head1, head2 = l1, prev
        
        while head2:
            nexxt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nexxt
        
            
            
            
            
        