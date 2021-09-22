from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_1 = Counter(s)
        t_1 = Counter(t)
        
        return (t_1 - s_1).popitem()[0]
            
        
        