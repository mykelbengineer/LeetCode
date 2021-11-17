class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = left = 0
        right = len(nums) - 1
        
        while curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1
                
                
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                
            else:
                curr += 1
                
                
        