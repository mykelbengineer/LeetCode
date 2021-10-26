# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return False
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        
        while slow:
            tmp = slow
            slow = slow.next
            tmp.next = prev
            prev = tmp
            
        
        while head and prev:
            if head.val != prev.val:
                return False
            
            head = head.next
            prev = prev.next
            
        
        return True
        
        