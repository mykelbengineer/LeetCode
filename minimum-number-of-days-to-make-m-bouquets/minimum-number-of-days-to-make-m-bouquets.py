class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m * k): return -1
        
        left = 1
        right = max(bloomDay)
        
        while left < right:
            mid = left + right >> 1
            count = 0 ## k
            bucket = 0 ## m
            
            for n in bloomDay:
                if n > mid:
                    count = 0  
                else:
                    count += 1
                    if count == k:
                        bucket += 1
                        count = 0
                        
                        if bucket == m:
                            break
            
            if bucket == m:
                right = mid
                
            else:
                left = mid + 1
                
        return left
