class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        
        for num in nums:
            if num - 1 not in nums_set:
                curr = num
                streak = 1
                
                
                while curr + 1 in nums_set:
                    curr += 1
                    streak += 1
                    
                
                longest = max(longest, streak)
                
                
        return longest