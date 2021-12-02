class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = right = longest = 0
        seen = defaultdict(int)
        
        while right < len(s):
            current_char = s[right]
            seen[current_char] += 1
            
            while left <= right and len(seen) > k:
                left_char = s[left]
                seen[left_char] -= 1
                if seen[left_char] <= 0:
                    del seen[left_char]
                
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
            
        return longest
        