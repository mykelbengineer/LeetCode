class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        intRep = 0
        mul = 1
        i = len(digits)
        
        while True:
            i -= 1
            if i < 0: break
            
            intRep = intRep + (digits[i] * mul)
            mul *= 10
            
        intRep += 1
        
        
        for i in str(intRep):
            output.append(i)
            
            
        return output