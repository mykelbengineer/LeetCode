class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        old_color = image[sr][sc]
        
        def dfs(i, j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return 
            
            if image[i][j] == newColor or image[i][j] != old_color:
                return 
            
            image[i][j] = newColor
            
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
            
        dfs(sr, sc)
        
        return image
        