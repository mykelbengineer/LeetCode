class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" : return 0
        
        lps = [0] * len(needle)
        prevLps, i = 0, 1
        
        while i < len(needle):
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
                
            elif prevLps == 0:
                lps[i] = 0
                i += 1
                
            else:
                prevLps = lps[prevLps - 1]
                
                
        i = 0
        j = 0
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i+1, j+1
                
            else:
                
                if j == 0:
                    i += 1
                    
                else:
                    j = lps[j - 1]
                    
            if j == len(needle):
                return i - len(needle)
            
            
        return -1
                