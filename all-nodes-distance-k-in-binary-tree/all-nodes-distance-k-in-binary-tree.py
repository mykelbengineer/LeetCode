# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def buildGraph(self, node, parent, graph):
        if not node:
            return
        
        if parent is not None:
            graph[node].append(parent)
            
        if node.left:
            graph[node].append(node.left)
            self.buildGraph(node.left, node, graph)
            
        if node.right:
            graph[node].append(node.right)
            self.buildGraph(node.right, node, graph)
            
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        graph, visited, ans = defaultdict(list), set(), []
        
        self.buildGraph(root, None, graph)
        
        q = [(target, 0)]
        
        while q:
            
            node, distance = q.pop(0)
            
            if node in visited:
                continue
                
            visited.add(node)
            
            
            if distance == K:
                ans.append(node.val)
                
            elif distance < K:
                for child in graph[node]:
                    q.append((child, distance+1))
                    
        return ans
                    
                
            
            
        
        
        