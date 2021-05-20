class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        N = len(nums)
        output = []
        
        for i in range(N):
            output.append(p)
            p *= nums[i]
            
        p = 1
        
        for i in range(N-1,-1,-1):
            output[i] = output[i] * p
            p *= nums[i]
            
        return output
        