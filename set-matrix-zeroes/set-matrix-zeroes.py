class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        def flip_row(index):
            for i in range(columns):
                if matrix[index][i] != 0:
                    matrix[index][i] = '*'
                    
        def flip_column(index):
            for i in range(rows):
                if matrix[i][index] != 0:
                    matrix[i][index] = '*'
                    
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    flip_row(i)
                    
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    flip_column(j)
                    
                    
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0
                    
                    
        
        
        