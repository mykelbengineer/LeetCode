class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        visited = set()
        self.path_str = ''
        
        def dfs(grid, i, j, path):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            self.path_str += path
            
            dfs(grid,i-1, j, 'up')
            dfs(grid,i+1, j, 'down')
            dfs(grid,i,j+1, 'right')
            dfs(grid,i,j-1, 'left')
            
            self.path_str += 'done'
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(grid,i,j,'start')
                    visited.add(self.path_str)
                    self.path_str = ''
                    
        return len(visited)
        