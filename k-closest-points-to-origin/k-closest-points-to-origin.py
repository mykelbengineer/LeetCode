import heapq as heap
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        results = []
        
​
        
        for point in points:
            dis = point[0] **2 + point[1] ** 2
            
            heap.heappush(results, (-dis, point))
            
            if len(results) > K:
                heap.heappop(results)
            
        
        
        return[point[1] for point in results]
            
