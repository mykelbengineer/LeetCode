class RandomizedSet:

    def __init__(self):
        self.data = []
        self.random_map = {} 

    def insert(self, val: int) -> bool:
        if val not in self.random_map:
            
            self.random_map[val] = len(self.data)
            
            self.data.append(val)
            
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.random_map:
            
            last_val = self.data[-1]
            last_val_index = self.random_map[last_val]
            
            remove_val_index = self.random_map[val]
            
            self.random_map[last_val] = remove_val_index
            self.data[remove_val_index] = last_val
            self.data[last_val_index] = val
            
            self.data.pop()
            self.random_map.pop(val)
            
            return True
        
        return False
            
        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()