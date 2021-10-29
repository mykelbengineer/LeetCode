class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = []
        nums_set = set(nums)
        
        for i in nums_set:
            if i - 1 not in nums_set:
                sc = 1
                n = i + 1
            
                while n in nums_set:
                    sc += 1
                    n += 1

                output.append(sc)
            
        
        return max(output) if output else 0