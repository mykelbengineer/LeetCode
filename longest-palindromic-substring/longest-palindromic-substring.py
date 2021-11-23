class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i, i+1), res, key=len)
            
        return res
        
        
    
    def helper(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
            
        return string[left + 1: right]
        