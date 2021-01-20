import collections
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counts = collections.Counter(hand)
        
        for n in sorted(counts):
            if not counts[n]:
                continue
            temp = counts[n]
            
            for i in range(n, n+W):
                if counts[i] < 1:
                    return False
                counts[i] -= temp
                
        return True
        
        
