class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        left = 0
        res = float(inf)
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            while curr_sum >= s:
                res = min(res, i+1 - left)
                curr_sum -= nums[left]
                left += 1
                
        
        if res == float(inf) : return 0
        else : return res
        
​
       
