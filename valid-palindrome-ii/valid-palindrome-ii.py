class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                
                return self.valid(s, i+1, j) or self.valid(s, i, j-1)
            
        
        return True
    
    
    def valid(self, s, i, j):
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                return False
            
        
        return True
        