class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = running_sum = 0
        mod_array = [1] + [0] * k
        
        for num in nums:
            
            running_sum += num
            
            result += mod_array[running_sum % k]
            
            mod_array[running_sum % k] += 1
            
            
        return result