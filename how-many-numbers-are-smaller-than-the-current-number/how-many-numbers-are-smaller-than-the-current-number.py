class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        counter = 0
        
        for i in range(n):
            for j in range(n):
                if nums[i] != nums[j] and nums[i] > nums[j]:
                    counter += 1
            
            output[i] = counter
            counter = 0
            
        
        return output
            
                    
        