from collections import deque
from collections import Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.counter = Counter(nums)
        self.unique = set()
        
        for i in nums:
            self.queue.append(i)
            
        for k, v in self.counter.items():
            if v == 1:
                self.unique.add(k)
            
    def showFirstUnique(self) -> int:
        if not self.unique:
            return -1
        
        for i in self.queue:
            if i in self.unique:
                return i
        

    def add(self, value: int) -> None:
        self.queue.append(value)
        
        if value in self.counter:
            self.counter[value] += 1
            
            if value in self.unique:
                self.unique.remove(value)
            
        else:
            self.counter[value] = 1
            self.unique.add(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)