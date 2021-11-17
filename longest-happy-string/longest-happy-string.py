class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count_chars = []
        if a:
            heapq.heappush(count_chars, (-a, 'a'))
        if b:
            heapq.heappush(count_chars, (-b, 'b'))
        if c:
            heapq.heappush(count_chars, (-c, 'c'))
            
        
        result = []
        
        while count_chars:
            fcount, first = heapq.heappop(count_chars)
            
            if len(result) >= 2 and result[-1] == result[-2] == first:
                if not count_chars:
                    return ''.join(result)
                
                scount, second = heapq.heappop(count_chars)
                result.append(second)
                
                scount += 1
                if scount != 0:
                    heapq.heappush(count_chars, (scount, second))
                    
                heapq.heappush(count_chars, (fcount, first))
                continue
                
            
            result.append(first)
            fcount += 1
            
            if fcount != 0: heapq.heappush(count_chars, (fcount, first))
        
        return ''.join(result)
                    