class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = deque([])
        
        def bfs(queue, grid):
            while queue:
                I, J = queue.popleft()
                for i, j in ([I-1, J], [I+1,J], [I, J-1], [I, J+1]):
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                        queue.append((i,j))
                        grid[i][j] = '0'
                        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i,j))
                    bfs(queue, grid)
                    count += 1
                    
                    
        return count 
                    
            
