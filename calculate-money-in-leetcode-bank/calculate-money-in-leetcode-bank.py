class Solution:
    def totalMoney(self, n: int) -> int:
        output = k = 0
        
        for num in range(n):
            if num % 7 == 0: k = num // 7
            
            k += 1
            
            output += k
            
        return output
        