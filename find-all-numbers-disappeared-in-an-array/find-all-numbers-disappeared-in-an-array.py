class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
                
        output = []
        for i, k in enumerate(nums):
            if k > 0:
                output.append(i+1)
                
        return output
                
        
        
        
        