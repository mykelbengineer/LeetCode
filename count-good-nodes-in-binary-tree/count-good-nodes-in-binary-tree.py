# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: return None
        numOfGood = 0
        stack = [(root, float(-inf))]
        
        while stack:
            
            node, directionMax = stack.pop()
            
            if node.val >= directionMax:
                numOfGood += 1
                
            if node.left:
                stack.append((node.left, max(node.val, directionMax)))
                
            if node.right:
                stack.append((node.right, max(node.val, directionMax)))
                
        return numOfGood
                
        
        
        