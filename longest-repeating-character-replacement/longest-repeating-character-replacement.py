class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Algorithm
        # We count each character in our window
        # We keep track of the max frequently occuring character
        # If there more characters than k in our window which is not the max frequently character
        # We reduce our window by removing s[left] from our counts
        # Increment left
        
        counts = defaultdict(int)
        left = maxF = res = 0
        
        for right in range(len(s)):
            counts[s[right]] += 1
            maxF = max(maxF, counts[s[right]])
            
            while (right - left + 1) - maxF > k:
                counts[s[left]] -= 1
                left += 1
                
                
            res = max(res, right - left + 1)
            
            
        return res
        