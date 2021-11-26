class Solution:
    def maxPower(self, s: str) -> int:
        longest = count = 1
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
                
            else:
                count = 1
                
            longest = max(longest, count)
            
        return longest
        