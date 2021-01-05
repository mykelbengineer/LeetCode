"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        curr_level = [root]
        
        while curr_level:
            level_nodes = []
            next_level = []
            
            for i in range(len(curr_level)):
                if i + 1 >= len(curr_level):
                    curr_level[i].next = None
                else:
                    curr_level[i].next = curr_level[i + 1]
                    
            
            for node in curr_level:
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                    
            
            curr_level = next_level
        
        return root
        
