class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        output = []
        
        for i in range(len(candies)):
            if extraCandies + candies[i] >= m:
                pass
                output.append(True)
            else:
                output.append(False)
                
        return output
        