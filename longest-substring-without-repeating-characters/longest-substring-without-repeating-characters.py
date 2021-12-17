class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Algorithm
        # Keep a set of numbers seen
        # If a number appears in a set more than once, we remove the left element and move left
        # Return the max window
        
        seen = set()
        left = longest = right = count = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                count += 1
                
                
            else:
                seen.remove(s[left])
                left += 1
                count -= 1
                
                
            longest = max(longest, count)
            
            
        return longest
        