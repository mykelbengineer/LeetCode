class Solution:

    def __init__(self, nums: List[int]):
        self.newArray = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        self.newArray = self.original
        self.original = list(self.original)
        return self.newArray
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.newArray)):
            rand = random.randrange(i,len(self.newArray))
            self.newArray[i], self.newArray[rand] = self.newArray[rand], self.newArray[i]
        return self.newArray
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()