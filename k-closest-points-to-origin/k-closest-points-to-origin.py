class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results, output = [], []
        
        for point in points:
            dis = point[0] * point[0] + point[1] * point[1]
            
            results.append((dis,point))
            
        
        results.sort(key = lambda x:x[0])
        
        print(results)
        
        for i in range(k):
            output.append(results[i][1])
            
        return output