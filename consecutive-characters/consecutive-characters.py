class Solution:
    def maxPower(self, s: str) -> int:
        seen = set()
        output = 0
        count = 0
        left = 0
        
        while left < len(s):
            if s[left] not in seen:
                seen.clear()
                seen.add(s[left])
                count = 1
                
            else:
                count += 1
                
            output = max(output, count)
            left += 1
        
        return output