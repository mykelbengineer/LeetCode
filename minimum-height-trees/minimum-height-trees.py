class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        totalNumNodes = n
        
        if totalNumNodes == 1:
            return [0]
        
        adjList = defaultdict(set)
        
        for node, edge in edges:
            adjList[node].add(edge)
            adjList[edge].add(node)
            
        
        leaveNodes = []
        
        for node in adjList:
            if len(adjList[node]) == 1:
                leaveNodes.append(node)
                
        
        while totalNumNodes > 2:
            
            totalNumNodes -= len(leaveNodes)
            
            nextLevelLeaveNodes = []
            
            for leaf in leaveNodes:
                
                neighbor = adjList[leaf].pop()
                adjList[neighbor].remove(leaf)
                
                if len(adjList[neighbor]) == 1:
                    nextLevelLeaveNodes.append(neighbor)
                    
            leaveNodes = nextLevelLeaveNodes
            
        return leaveNodes