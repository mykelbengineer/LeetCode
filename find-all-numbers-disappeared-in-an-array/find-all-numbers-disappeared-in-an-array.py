class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        
        # loop through the array and mark nums[i] negative to indicate visited
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            
            if nums[temp] > 0:
                nums[temp] *= -1
                
        for index, value in enumerate(nums):
            if value > 0:
                output.append(index + 1)
                
                
        return output
                
        
        