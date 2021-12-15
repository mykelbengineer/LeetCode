class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        def flipRow(index):
            for i in range(cols):
                if matrix[index][i] != 0:
                    matrix[index][i] = '*'
                    
        def flipCol(index):
            for i in range(rows):
                if matrix[i][index] != 0:
                    matrix[i][index] = '*'
                    
                    
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    flipRow(i)
                    
                    
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    flipCol(j)
                    
                    
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0
                    
                    
        
                    
        
        