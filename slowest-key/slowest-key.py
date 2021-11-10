class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        t, k = releaseTimes[0], keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > t or (time == t and keysPressed[i] > k):
                t = time
                k = keysPressed[i]
                
        return k
            
            
        