class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d_logs = []
        l_logs = []
        
        
        for log in logs:
            if log.split()[1].isdigit():
                d_logs.append(log)
                
            else:
                l_logs.append(log)
                
        l_logs = sorted(l_logs, key=lambda x:x.split()[0]) # Sort by identifiers
        l_logs = sorted(l_logs, key=lambda x:x.split()[1:]) # Sort by suffix
        
        return l_logs + d_logs