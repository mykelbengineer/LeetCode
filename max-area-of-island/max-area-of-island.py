class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = max(count,self.dfs(grid, i, j))
                    
        return count
    
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        
        up = self.dfs(grid, i-1,j)
        down = self.dfs(grid, i+1,j)
        left = self.dfs(grid, i,j-1)
        right = self.dfs(grid, i,j+1)
        
        return 1 + up + down + left + right
        
        
                    