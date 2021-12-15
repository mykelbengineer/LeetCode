class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        left = right = 0
        seen = set()
        longest = count = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                count += 1
                right += 1
                
            else:
                seen.remove(s[left])
                left += 1
                count -= 1
                
            longest = max(longest, count)
            
        return longest