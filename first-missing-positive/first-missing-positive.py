class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_sort = sorted(list(set(nums)))
        
        res = 1
        
        for num in nums_sort:
            if num == res:
                res += 1
                
        return res
        
    