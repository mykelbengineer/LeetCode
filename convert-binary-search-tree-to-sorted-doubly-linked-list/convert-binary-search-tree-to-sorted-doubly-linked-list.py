"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        
        
        def helper(node):
            nonlocal first, last
            
            if node:
                helper(node.left)
                
                if last:
                    last.right, node.left = node, last
                    
                else:
                    first = node
                    
                last = node
                helper(node.right)
                
        first, last = None, None       
        helper(root)
        first.left, last.right = last, first
        
        return first
        