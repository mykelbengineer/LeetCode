class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_count = len(matrix)
        column_count = len(matrix[0])
        
        def flip_row(pos):
            for i in range (column_count):
                if matrix[pos][i] != 0:
                    matrix[pos][i] = "*"
​
        def flip_column(pos):
            for j in range (row_count):
                if matrix[j][pos] != 0:
                    matrix[j][pos] = "*"
        
        for i in range(row_count):
            for j in range(column_count):
                if matrix[i][j] == 0:
                    flip_row(i)
                    break
        
        for j in range(column_count):
            for i in range(row_count):
                if matrix[i][j] == 0:
                    flip_column(j)
                    break
                    
        for i in range(row_count):
            for j in range(column_count):
                if matrix[i][j] == "*":
                    matrix [i][j] = 0
                    
    
​
            
        
