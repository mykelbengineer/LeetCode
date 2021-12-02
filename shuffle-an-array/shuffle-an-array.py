class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.backup = list(nums)
        

    def reset(self) -> List[int]:
        self.original = self.backup
        self.backup = list(self.original)
        return self.original
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.original)):
            rand = random.randrange(i, len(self.original))
            self.original[rand], self.original[i] = self.original[i], self.original[rand]
            
        return self.original
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()