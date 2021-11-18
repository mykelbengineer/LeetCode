class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        elements = []
        count = 1
        
        for i in nums:
            heapq.heappush(elements, -i)
            
        
        while count != k:
            heapq.heappop(elements)
            count += 1
            
        kLargest = heapq.heappop(elements)
        return -kLargest