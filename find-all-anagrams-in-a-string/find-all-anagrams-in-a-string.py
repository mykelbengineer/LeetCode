class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        pCount = defaultdict(int)
        sCount = defaultdict(int)
        res = []
        left = 0
        
        for i in range(len(p)):
            pCount[p[i]] += 1
            sCount[s[i]] += 1
            
        res.append(0) if sCount == pCount else []
        
        for r in range(len(p), len(s)):
            sCount[s[r]] += 1
            sCount[s[left]] -= 1
            
            if sCount[s[left]] == 0:
                del sCount[s[left]]
                
            left += 1
            
            if sCount == pCount:
                res.append(left)
                
        return res
        
        
