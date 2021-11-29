class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        output = []
        chars = Counter(S)
        
        for key, val in chars.items():
            heapq.heappush(heap, (-val , key))
            
        while heap:
            fNum , fChar = heapq.heappop(heap)
            
            if output and output[-1] == fChar:
                if heap:
                    sNum, sChar = heapq.heappop(heap)
                    
                    output.append(sChar)
                    sNum += 1
                    
                    if sNum != 0:
                        heapq.heappush(heap, (sNum, sChar))
                    
                    heapq.heappush(heap, (fNum, fChar))
                    continue
                    
                else:
                    return ''
                
            else:
                
                output.append(fChar)
                fNum += 1
                
                if fNum != 0:
                    heapq.heappush(heap, (fNum,fChar))
                    
        return ''.join(output)
                    
            
            
        