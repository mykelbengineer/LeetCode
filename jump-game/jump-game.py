class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = n - 1
        
        for i in range(n-1,-1,-1):
            if i + nums[i] >= pos:
                pos = i
                
        
        return pos == 0
                
            

        