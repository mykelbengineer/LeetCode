class Solution:
    def maxPower(self, s: str) -> int:
        count = max_count = 0
        prev = None
        
        for char in s:
            if char == prev:
                count += 1
                
            else:
                count = 1
                prev = char
            
            max_count = max(max_count, count)
            
        
        return max_count
        