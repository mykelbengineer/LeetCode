class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h_map = {}
        output = []
        size = end = 0
        
        for i, k in enumerate(s):
            h_map[k] = i
            
            
        for i, k in enumerate(s):
            size += 1
            end = max(end, h_map[k])
            
            if i == end:
                output.append(size)
                size = 0
                
            
            
        return output
            
            
            
        
        