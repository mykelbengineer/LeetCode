class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1
        
        if nums[left] > nums[right]:
            return self.isDecreasing(nums)
        
        else:
            return self.isIncreasing(nums)
        
    def isDecreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                return False
            
        return True
    
    def isIncreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
            
        return True
        