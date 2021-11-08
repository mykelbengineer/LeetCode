class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            curr_cap = 0
            num_ships = 1
            
            for w in weights:
                curr_cap += w
                if curr_cap > mid:
                    curr_cap = w
                    num_ships += 1
                    
            if num_ships > days:
                left = mid + 1
                
            else:
                right = mid
                
        return left
                
                