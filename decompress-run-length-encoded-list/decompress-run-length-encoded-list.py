class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        
        i = 0
        j = 1
        
        while j < len(nums):
            a = nums[i]
            b = nums[j]
            
            for _ in range(a):
                output.append(b)
                
            i += 2
            j += 2
            
        return output
        