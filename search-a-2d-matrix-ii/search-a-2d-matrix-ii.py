class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix:
        
            row, width = len(matrix) - 1, len(matrix[0])
            col = 0
​
            while row >= 0 and col < width:
​
                if matrix[row][col] == target:
                    return True
​
                elif matrix[row][col] > target:
​
                    row = row - 1
​
                else:
​
                    col = col + 1
​
            return False
        
