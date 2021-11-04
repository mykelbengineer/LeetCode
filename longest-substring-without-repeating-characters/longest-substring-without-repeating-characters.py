class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_count = 0
        seenChars = set()
        N = len(s)
        
        while left < N and right < N:
            if s[right] not in seenChars:
                seenChars.add(s[right])
                right += 1
                max_count = max(max_count, right - left)
                
            else:
                seenChars.remove(s[left])
                left += 1
                
        return max_count
            
            
        
        