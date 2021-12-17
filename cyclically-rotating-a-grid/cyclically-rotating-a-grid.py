class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        top, left = 0, 0
        bottom, right = m - 1, n - 1
        
        while top < bottom and left < right:
            element_count = 2 * (bottom - top + 1) + 2 * (right - left + 1) - 4
            net_rotations = k % element_count
        
            for _ in range(0, net_rotations):
                temp = grid[top][left]

                for j in range(left, right):
                    grid[top][j] = grid[top][j + 1]

                for i in range(top, bottom):
                    grid[i][right] = grid[i + 1][right]

                for j in range(right, left, -1):
                    grid[bottom][j] = grid[bottom][j - 1]

                for i in range(bottom, top, -1):
                    grid[i][left] = grid[i - 1][left]

                grid[top + 1][left] = temp
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return grid