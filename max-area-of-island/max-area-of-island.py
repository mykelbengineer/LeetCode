class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        def dfs(i,j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            up = dfs(i-1, j, grid)
            down = dfs(i+1, j, grid)
            left = dfs(i,j-1, grid)
            right = dfs(i, j+1, grid)
            
            return up + down + left + right + 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    
                    count = max(dfs(i,j,grid), count)
                    
        
        return count
                    
                   
                    