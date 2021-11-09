class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        output = []
        
        last_seen_start = sorted_intervals[0][0]
        last_seen_end = sorted_intervals[0][1]
        
        for i in range(1, len(sorted_intervals)):
            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]
            
            if start <= last_seen_end:
                last_seen_end = max(end, last_seen_end)
                continue
                
            else:
                output.append(list((last_seen_start, last_seen_end)))
                last_seen_start = start
                last_seen_end = end
        output.append(list((last_seen_start, last_seen_end)))     
        return output
                
                
                
        
        
        