from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        
        for k,v in count.items():
            if v > 1:
                return True
            
        return False
        