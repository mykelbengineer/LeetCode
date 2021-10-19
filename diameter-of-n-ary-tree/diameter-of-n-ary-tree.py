"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        self.ans = 0
        
        def dfs(node):
            
            if not node: return 0
            
            max_height_1 = 0
            max_height_2 = 0
            
            for child in node.children:
                parent_height = dfs(child) + 1
                
                if parent_height > max_height_1:
                    max_height_1, max_height_2 = parent_height, max_height_1
                    
                elif parent_height > max_height_2:
                    max_height_2 = parent_height
                    
            distance = max_height_1 + max_height_2
            
            self.ans = max(self.ans, distance)
            
            return max_height_1
        
        
        dfs(root)
        
        return self.ans
            
            