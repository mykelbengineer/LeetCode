import heapq as heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map = {}
        
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        return heap.nlargest(k, nums_map, key= nums_map.get)
        
