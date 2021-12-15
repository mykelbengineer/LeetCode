class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        output = []
        direction = 0
        
        while left <= right and top <= bottom:
            
            if direction == 0:
                for i in range(left, right+1):
                    output.append(matrix[top][i])
                    
                top += 1
                
                
            elif direction == 1:
                for i in range(top, bottom+1):
                    output.append(matrix[i][right])
                    
                right -= 1
                
                
            elif direction == 2:
                for i in range(right, left-1, -1):
                    output.append(matrix[bottom][i])
                    
                bottom -= 1
                
                
            else:
                for i in range(bottom, top-1, -1):
                    output.append(matrix[i][left])
                
                left += 1
                
                
            direction = (direction + 1) % 4
            
            
        return output
                    
        
        