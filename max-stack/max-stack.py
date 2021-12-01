class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.soft = set()
        self.id = 0
        
        
    def _soft_delete(self):
        while self.stack and self.stack[-1][1] in self.soft:
            self.soft.remove(self.stack.pop()[1])
        while self.heap and self.heap[0][1] in self.soft:
            self.soft.remove(heapq.heappop(self.heap)[1])

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, self.id))
        self.stack.append((x, self.id))
        self.id -= 1
        
        
        

    def pop(self) -> int:
        if self.stack:
            element, key = self.stack.pop()
            self.soft.add(key)
            self._soft_delete()
            
            return element
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def peekMax(self) -> int:
        if self.heap:
            return -self.heap[0][0]
        

    def popMax(self) -> int:
        if self.stack and self.heap:
            element, key = heapq.heappop(self.heap)
            self.soft.add(key)
            self._soft_delete()
            
            return -element
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()