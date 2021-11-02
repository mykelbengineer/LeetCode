"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        oldToNewMap = {}
        
        def dfs(node):
            if node in oldToNewMap:
                return oldToNewMap[node]
            
            copy = Node(node.val)
            oldToNewMap[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
        
        
        return dfs(node)
