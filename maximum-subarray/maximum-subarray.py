class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_current = max_global = nums[0]
        
        for i in range(1, len(nums)):
            max_current = max(max_current + nums[i], nums[i])
            if max_current > max_global:
                max_global = max_current
                
        return max_global
        
        
        
        
