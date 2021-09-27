class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = [0] * len(nums)
        
        for i in range(len(nums)):
            n[i] = nums[nums[i]]
            
        return n
        