class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        
        def back_tracking(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            
            
            if i >= len(s) and j >= len(p): return True
            if j >= len(p) : return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if (j+1) < len(p) and p[j+1] == '*':
                cache[(i,j)] = back_tracking(i, j+2) or (match and back_tracking(i+1, j))
                return cache[(i,j)]
            
            
            if match:
                cache[(i,j)] = back_tracking(i+1, j+1)
                return cache[(i,j)]
            
            
            cache[(i,j)] = False
            return False
        
        
        
        return back_tracking(0,0)
            
        