# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        current_level = [root]
        total_levels = 0
        
        while current_level:
            level_nodes = []
            next_level = []
            
            for node in current_level:
                level_nodes.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            total_levels += 1
            current_level = next_level
            
        return total_levels
        
        
