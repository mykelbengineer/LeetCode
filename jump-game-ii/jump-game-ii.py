class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        i,max_pos,last_pos,jump = 0,0,0,0
        
        while i < N-1:
            max_pos = max(max_pos, i + nums[i])
            
            if i == last_pos:
                last_pos = max_pos
                jump += 1
                
            i += 1
            
        
        return jump
        