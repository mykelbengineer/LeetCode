class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        counter = right = len(nums) - 1
        output = [0] * len(nums)

        while left <= right:
            
            if nums[left] * nums[left] > nums[right] * nums[right]:
                output[counter] = nums[left] * nums[left]
                left += 1
                
            else:
                output[counter] = nums[right] * nums[right]
                right -= 1
                
            counter -= 1
            
            
        return output