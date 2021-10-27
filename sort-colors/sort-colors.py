class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = curr = 0
        R = len(nums) - 1
        
        while curr <= R:
            if nums[curr] == 0:
                nums[L], nums[curr] = nums[curr], nums[L]
                curr += 1
                L += 1
                
            elif nums[curr] == 2:
                nums[R], nums[curr] = nums[curr], nums[R]
                R -= 1
                
            else:
                curr += 1
        
        
        
        