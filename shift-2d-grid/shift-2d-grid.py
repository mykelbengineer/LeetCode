class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for _ in range(k):
            previous = grid[-1][-1]
            for i in range(num_rows):
                for j in range(num_cols):
                    temp = grid[i][j]
                    grid[i][j] = previous
                    previous = temp
                
        return grid
        