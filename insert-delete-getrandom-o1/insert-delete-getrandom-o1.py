class RandomizedSet:

    def __init__(self):
        self.rand_set = list()

    def insert(self, val: int) -> bool:
        if val not in self.rand_set:
            self.rand_set.append(val)
            return True
        return False
            

    def remove(self, val: int) -> bool:
        if val in self.rand_set:
            self.rand_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        rand_index = random.randrange(len(self.rand_set))
        return self.rand_set[rand_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()