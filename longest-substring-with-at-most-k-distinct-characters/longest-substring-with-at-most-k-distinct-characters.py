class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest_substring = 0
        left, right = 0, 0
        seen = defaultdict(int)        
        
        while right < len(s):
            seen[s[right]] += 1
            
            while left <= right and len(seen) > k:
                left_char = s[left]
                seen[left_char] -= 1
                if seen[left_char] == 0:
                    del seen[left_char]
                left += 1
                
            longest_substring = max(longest_substring, right-left+1)
            right += 1
        
        return longest_substring
                
                