class TwoSum:

    def __init__(self):
        self.array = {}
        
    def add(self, number: int) -> None:
        if number in self.array:
            self.array[number] += 1
            
        else:
            self.array[number] = 1
        
    def find(self, value: int) -> bool:
        for num in self.array.keys():
            comp = value - num
            if comp != num:
                if comp in self.array:
                    return True
                
            else:
                if self.array[comp] > 1:
                    return True
                
        return False
                    
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)