class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
                            
                    
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            
            up = dfs(grid,i+1,j)
            left = dfs(grid,i,j-1)
            right = dfs(grid,i,j+1)
            down = dfs(grid,i-1,j)
            
            return up + left + right + down + 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(count, dfs(grid, i,j))

        return count
        
        