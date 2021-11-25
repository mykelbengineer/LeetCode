class Solution:
    def reverse(self, x: int) -> int:
        flag = result = 0
        lowest = -1 * ((2**31) - 1)
        highest = 1 * ((2**31) - 1)
        
        if x < 0 : 
            flag = 1
            x = x * -1
            
        while True:
            
            result = result * 10 + x % 10
            x = x // 10
            
            if not x: break
                
                
        if flag:
            result *= -1
            
        return result if lowest < result < highest else 0
        