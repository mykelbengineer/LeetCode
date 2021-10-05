class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        
        if target > nums[R]:
            return len(nums)
        
        while L <= R:
            mid = (L + R) //2
            
            mid_val = nums[mid]
            
            if target == mid_val:
                return mid
            
            elif target > mid_val:
                L = mid + 1
                
            else:
                R = mid - 1
        
        return L
        