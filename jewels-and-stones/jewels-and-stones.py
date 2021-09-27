from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = Counter(stones)
        output = 0
        
        for i in jewels:
            if i in stones:
                output += n[i]
                
        return output
        
        