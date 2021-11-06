class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = nums

    def sumRange(self, left: int, right: int) -> int:
        output = 0
        for i in range(left, right+1):
            output += self.nums_array[i]
        return output
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)