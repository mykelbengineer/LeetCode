class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,N):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])
            
            
        return min(dp[N-1], dp[N-2])
            
        
        