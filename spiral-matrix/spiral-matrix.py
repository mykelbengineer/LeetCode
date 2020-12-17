class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        direction = 0
        
        res = []
        
        while( top <= bottom and left <= right):
            
            if direction == 0:
                
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top += 1
                    
            
            elif direction == 1:
                
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
                
                
            elif direction == 2:
                
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                
            elif direction == 3:     
                
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            
            direction = (direction + 1) % 4
            
        
        return res
                
            
