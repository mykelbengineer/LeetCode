class Solution:
    def dfs(self, graph, visited, pos):
        for i in range(len(graph)):
            if graph[pos][i] == 1 and visited[i] == 0:
                visited[i] = 1
                self.dfs(graph, visited, i)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = [0] * len(isConnected)
        count = 0
        
        for i in range(len(isConnected)):
            if seen[i] == 0:
                self.dfs(isConnected, seen, i)
                count += 1
                
        return count
        
        