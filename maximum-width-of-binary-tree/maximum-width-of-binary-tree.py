# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        max_width = 0
        index = 0
        stack = [(root, index)]
        
        while stack:
            next_level = []
            
            max_width = max(max_width, stack[-1][1] - stack[0][1] + 1)
            
            for node, index in stack:
            
                if node.left:

                    next_level.append((node.left, index * 2))

                if node.right:

                    next_level.append((node.right, index * 2 + 1))
                    
            stack = next_level
                
        return max_width
        