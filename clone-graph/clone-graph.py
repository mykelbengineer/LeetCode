"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        
        c_map = {node: Node(node.val)}
        stack = [node]
        
        while stack:
            
            curr = stack.pop()
            
            for neigh in curr.neighbors:
                if neigh not in c_map:
                    c_map[neigh] = Node(neigh.val)
                    stack.append(neigh)
                    
                c_map[neigh].neighbors.append(c_map[curr])
            
        return c_map[node]
        
        
        