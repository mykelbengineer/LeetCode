# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        current_level = [root]
        result = []
        
        while current_level:
            level_nodes = []
            next_level = []
            
            for node in current_level:
                level_nodes.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            result.append(sum(level_nodes)/len(level_nodes))
            current_level = next_level
        return result
        
