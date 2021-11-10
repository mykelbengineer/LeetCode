class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        elements = [0] * 60
        
        for t in time:
            ans = ans + elements[-t % 60]
            elements[t % 60] = elements[t % 60] + 1
        return ans
        
        