class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        output = []
        i = 0
        j = 1
        
        while j < len(nums):
            for _ in range(nums[i]):
                output.append(nums[j])
                
            i += 2
            j += 2
            
            
        return output
            
        