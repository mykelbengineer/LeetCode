class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
​
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = nums[mid]
            
            if mid_val == target:
                return mid
            
            elif target < mid_val:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return -1 
        
                
