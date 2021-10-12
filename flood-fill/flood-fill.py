class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r = len(image)
        l = len(image[0])
        color = image[sr][sc]
        
        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= l:
                return
            
            if image[i][j] == newColor or image[i][j] != color:
                return
            
            image[i][j] = newColor
            dfs(i,j-1)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
            
        dfs(sr, sc)
        
        return image
    
    