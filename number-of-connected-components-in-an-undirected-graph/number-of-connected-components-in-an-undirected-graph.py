class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = [[] for _ in range(n)]
        
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
            
            
        stack = []
        seen = set()
        output = 0
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                stack.append(i)
                
                while stack:
                    
                    node = stack.pop()
                    
                    for nei in adjList[node]:
                        if nei in seen:
                            continue
                            
                        seen.add(nei)
                        stack.append(nei)
                        
                output += 1
            
            
        
        return output
        
        