# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        
        if not root:
            return True
        
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if not left and not right:
            return True
​
        if not left or not right:
            return False
​
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
​
            return outPair and inPair
        else:
​
            return False
        
        
        
​
       
​
        
        
       
