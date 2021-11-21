# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        midNode = self.getMid(head)
        root = TreeNode(midNode.val)
        
        if head == midNode: return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(midNode.next)
        
        return root
        
    
    def getMid(self, head):
        slow = dummy = ListNode(None)
        fast = dummy.next = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        return mid