class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        
        
        
        if not edges: return 0
        
        self.ans = 0
        adjList = {n:[] for n in range(len(edges) + 1)}
        
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
            
        def dfs(node, parent):
            
            max_height_1, max_height_2 = 0, 0
            
            for nei in adjList.get(node):
                if nei == parent:
                    continue
                    
                parent_height = dfs(nei, node)
                
                if max_height_1 < max_height_2:
                    max_height_1 = max(max_height_1, parent_height)
                else:
                    max_height_2 = max(max_height_2, parent_height)
            
            distance = max_height_1 + max_height_2
            
            self.ans = max(self.ans, distance)
            
            return max(max_height_1, max_height_2) + 1
        
        
        dfs(0, None)
        
        return self.ans