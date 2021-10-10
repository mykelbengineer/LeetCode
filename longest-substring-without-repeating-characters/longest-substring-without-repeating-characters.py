class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L  = R = Count = 0
        N = len(s)
        m_map = set()
        
        
        while L < N and R < N:
            if s[R] not in m_map:
                m_map.add(s[R])
                R += 1
                Count = max(Count, R - L)
                
            else:
                m_map.remove(s[L])
                L += 1
                
        return Count
        
                
                
            
            
        
        