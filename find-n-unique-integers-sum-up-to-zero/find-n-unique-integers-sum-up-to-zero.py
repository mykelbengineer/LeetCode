class Solution:
    def sumZero(self, n: int) -> List[int]:
        is_odd = n % 2
        half_of_n = n // 2
        
        if is_odd != 0:
            ans = [0]
            
        else:
            ans = []

        
        for i in range(1, half_of_n+1):
            ans.append(i)
            ans.append(-i)
            
        return ans