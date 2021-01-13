class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        count = 0
        close = float(-inf)
        
        for i in intervals:
            if i[0] >= close:
                close = i[1]
            else:
                count += 1
                
        return count
            
        
