class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = []
        cum_sum = 0
        left = 0
        
        for r in range(len(nums)):
            cum_sum += nums[r]
            
            while cum_sum >= target:
                output.append(r+1 - left)
                cum_sum -= nums[left]
                left += 1
        
        
        return min(output) if output else 0