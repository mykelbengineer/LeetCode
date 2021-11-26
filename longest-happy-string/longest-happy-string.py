class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars_heap = []
        if a: heapq.heappush(chars_heap, (-a, 'a'))
        if b: heapq.heappush(chars_heap, (-b, 'b'))
        if c: heapq.heappush(chars_heap, (-c, 'c'))
            
        output = []
        
        while chars_heap:
            max_count, max_char = heapq.heappop(chars_heap)
            
            if len(output) >= 2 and output[-1] == output[-2] == max_char:
                if not chars_heap: return ''.join(output)
                
                next_count, next_char = heapq.heappop(chars_heap)
                
                output.append(next_char)
                next_count += 1
                
                if next_count != 0:
                    heapq.heappush(chars_heap,(next_count, next_char))
                    
                heapq.heappush(chars_heap,(max_count, max_char))
                continue
                
            output.append(max_char)
            max_count += 1
            
            if max_count != 0:
                heapq.heappush(chars_heap,(max_count, max_char))
                
        return ''.join(output)
                
            
        
        
        