class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_all_nums = n * (n + 1) // 2
        sum_of_all_present = sum(nums)
        
        return sum_of_all_nums - sum_of_all_present