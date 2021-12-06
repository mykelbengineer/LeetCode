class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # move all odd chips to n - 1 or n + 1 or 1
        # move all even chips to n - 2 or n + 2 or 2
        
        # After that, check the smallest between the two and move one on top of the other
        even_cnt = 0
        odd_cnt = 0
        for i in position:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return min(even_cnt, odd_cnt)
        
        