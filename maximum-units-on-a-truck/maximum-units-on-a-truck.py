class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        ans = 0
        
        for box, val in sorted(boxTypes , key=lambda x:x[1], reverse=True):
            if count + box <= truckSize:
                ans += (box * val)
                count += box
                
            else:
                ans += (truckSize - count) * val
                return ans
            
        return ans
                
        
        