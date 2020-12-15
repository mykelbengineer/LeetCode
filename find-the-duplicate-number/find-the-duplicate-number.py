class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
                
        for k, v in map.items():
            if v >= 2:
                return k
        
