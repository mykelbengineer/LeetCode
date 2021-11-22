class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
    
        global_max = min_max = max_max = nums[0]
        
        for i in range(1, len(nums)):
            x = max(nums[i], min_max * nums[i], max_max * nums[i])
            y = min(nums[i], min_max * nums[i], max_max * nums[i])
            max_max, min_max = x, y
            global_max = max(max_max, global_max)
            
        return global_max