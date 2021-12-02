# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        
        output = 0
        
        stack = [(root, root.val)]
        
        while stack:
            
            node, curr_sum = stack.pop()
            
            if not node.left and not node.right:
                output += curr_sum
                
                
            if node.left:
                stack.append((node.left, curr_sum * 10 + node.left.val))
                
            if node.right:
                stack.append((node.right, curr_sum * 10 + node.right.val))
                
        return output
        