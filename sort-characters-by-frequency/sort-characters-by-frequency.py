class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        output = []
        counts = Counter(s)
        
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))
        
        while heap:
            val, key = heapq.heappop(heap)
            
            temp = key * (val * -1)
            output.append(temp)
            
            
        return ''.join(output)