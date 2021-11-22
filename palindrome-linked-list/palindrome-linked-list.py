# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # break list into two
        dummy = slow = ListNode(None)
        fast = dummy.next = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        # reverse second list
        
        prev = None
        
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
            
            
        # compare the two lists
        
        while head and prev:
            if head.val != prev.val:
                return False
            
            head = head.next
            prev = prev.next
            
        
        return True
        