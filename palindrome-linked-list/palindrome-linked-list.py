# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        prev = None
        
        while slow:
            cur = slow
            slow = slow.next
            cur.next = prev
            prev = cur
            
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
