class NumMatrix:

    def __init__(self, matrix: List[List[int]]):    
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j]
                
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i][j-1] + matrix[i][j]
                
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        current_sum = self.matrix[row2][col2]
        
        original = self.matrix[row1-1][col1 -1] if col1 != 0 and row1 != 0 else 0
        left = self.matrix[row2][col1-1] if col1 != 0 else 0
        top = self.matrix[row1-1][col2] if row1 != 0 else 0
        
        return current_sum - left - top + original
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)