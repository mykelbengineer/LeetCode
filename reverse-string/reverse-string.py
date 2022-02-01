class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(s, indX, indY):
            
            if indX >= (len(s) // 2): return
            
            s[indX], s[indY] = s[indY], s[indX]
            
            return reverse(s, indX + 1, indY - 1)
        
        
        reverse(s,0, len(s)-1)
        