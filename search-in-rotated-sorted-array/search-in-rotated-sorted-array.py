class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            comparator = nums[mid]
            
            if target < nums[0] and nums[mid] < nums[0]  or target >= nums[0] and nums[mid] >= nums[0]:
                
                comparator = nums[mid]
                
            else:
                
                if target < nums[0]:
                    
                    comparator = -inf
                    
                else:
                    
                    comparator = inf
                    
            if target == comparator : return mid
            
            if target > comparator :
                
                left = mid + 1
                
            else:
                
                right = mid - 1
                
                
        
        return -1
        
        