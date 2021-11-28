class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        
        intervals.sort(key=lambda x:x[0])
        last_meeting_end = intervals[0][1]
        
        
        for i in range(1, len(intervals)):
            meeting_start_time = intervals[i][0]

            if last_meeting_end > meeting_start_time:
                return False
            
            last_meeting_end = intervals[i][1]
            
        
        return True
        