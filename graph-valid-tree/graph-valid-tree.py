class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        
        adjList = [[] for _ in range(n)]
        
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        
        stack = [0]
        seen = {0}
        
        while stack:
            node = stack.pop()
            
            for nei in adjList[node]:
                if nei in seen:
                    continue
                seen.add(nei)
                stack.append(nei)
                
        
        return len(seen) == n