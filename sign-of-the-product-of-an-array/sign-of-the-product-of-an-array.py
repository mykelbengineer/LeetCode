class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        
        product = 1
        
        for i in nums:
            product *= i
            
        if product > 0: return 1
        elif product < 0: return -1
        else: return 0
        