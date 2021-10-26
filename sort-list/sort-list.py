# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode: 
        if not head or not head.next: return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    
    
    
    def getMid(self, node):
        slow = fast = node
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        return mid
    
    
    def merge(self, leftNode, rightNode):
        dummy = tail = ListNode(None)
        
        while leftNode and rightNode:
            if leftNode.val < rightNode.val:
                tail.next, tail, leftNode = leftNode, leftNode, leftNode.next

            else:
                tail.next, tail, rightNode = rightNode, rightNode, rightNode.next
            
        tail.next = leftNode or rightNode
        
        return dummy.next
        
        

            