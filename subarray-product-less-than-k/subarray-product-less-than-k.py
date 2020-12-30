class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  return 0
        
        start = end = res = 0
        n = len(nums)
        prod = 1
        
        while end < n:
            prod *= nums[end]
            
            while prod >= k:
                prod /= nums[start]
                start += 1
            
            sub_len = (end - start) + 1
            
            res += sub_len
            
            end += 1
            
        return res
                
                
