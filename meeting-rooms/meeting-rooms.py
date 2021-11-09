class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        sorted_intervals = sorted(intervals , key = lambda x:x[0])
    
        last_end_time = sorted_intervals[0][1]
        for i in range(1, len(intervals)):
            meeting_start = sorted_intervals[i][0]
            
            if meeting_start >= last_end_time:
                last_end_time = sorted_intervals[i][1]
                continue
                
            else:
                return False
            
            
        return True
            
            
        