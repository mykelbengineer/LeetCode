class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        
        dp = [1] * n
        dp[0] = 0
        dp[1] = 0
        
        i = 2
        
        while i < n:
            tmp = i
            if dp[i]:
                tmp += i
                while tmp < n:
                    dp[tmp] = 0
                    tmp += i
            i += 1
            
        return sum(dp)
        
        
        