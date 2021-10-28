class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        output = []
        
        for i in range(n):
            output.append(p)
            p = p * nums[i]
            
        p = 1
        
        for i in range(n-1,-1,-1):
            output[i] = p * output[i]
            p = p * nums[i]
            
        
        return output