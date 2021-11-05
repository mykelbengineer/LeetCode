class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) : return False
        
        left = 0
        s1Counter = defaultdict(int)
        s2Counter = defaultdict(int)
        
        for i in range(len(s1)):
            s1Counter[s1[i]] += 1
            s2Counter[s2[i]] += 1
            
        if s1Counter == s2Counter: return True 
    
        for r in range(len(s1), len(s2)):
            s2Counter[s2[r]] += 1
            s2Counter[s2[left]] -= 1
            
            if s2Counter[s2[left]] == 0:
                del s2Counter[s2[left]]
            
            left += 1
                
            if s2Counter == s1Counter:
                return True
            
        
        return False
            
        