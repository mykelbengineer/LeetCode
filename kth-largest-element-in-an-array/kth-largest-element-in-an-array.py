class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
            
        kLargest = 0
        
        for _ in range(k):
            kLargest = heapq.heappop(maxHeap)
            
            
        return -kLargest
            