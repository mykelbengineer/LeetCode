class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s_array = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        n = len(nums)
​
​
        for i in range(n-1, -1,-1):
            if nums[left] * nums[left] > nums[right] * nums[right]:
                s_array[i] = nums[left] * nums[left]
                left += 1
            else:
                s_array[i] = nums[right] * nums[right]
                right -= 1
​
        return s_array
