class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = {}
        
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            else:
                nums_map[i] += 1
                
        return max(nums_map, key=nums_map.get)   
