class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = max_cost = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                max_cost = 0
            res += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        return res
    
    
    
    
    
    
    
    
    # Algorithm
    # Loop through the colors
    # Keep a variable that you can compare current with
    # If curr == prev, check the value of curr and prev and pop the min
    # Check if the colors is colorful
    # If yes, return sum of output.
    # If no, repeat 
    
    
    
    
        