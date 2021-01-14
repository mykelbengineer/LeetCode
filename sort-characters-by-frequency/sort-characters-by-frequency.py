import heapq as heap
class Solution:
    def frequencySort(self, s: str) -> str:
        
        output = []
        res = []
        s_map = {}
        
        for string in s:
            if string not in s_map:
                s_map[string] = 1
            
            else:
                
                s_map[string] += 1
                
        
        for key, val in s_map.items():
            heap.heappush(res, (-val, key))
            
          
        while res:
            value, key = heap.heappop(res)
            output += [key] * -value
            
        return ''.join(output)
            
            
            
        
        
        
