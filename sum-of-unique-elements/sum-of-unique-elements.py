class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        output = 0
        
        for num in nums:
            seen[num] += 1
            
        
        for k, v in seen.items():
            if v == 1:
                output += k
                
                
        return output
        