class MaxStack:

    def __init__(self):
        self.soft_delete = set()
        self.stack = []
        self.max_heap = []
        self.id = 0
        

    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.id))   
        self.stack.append((x, self.id))
        self.id -= 1
        
    def _clean_up(self):
        while self.stack and self.stack[-1][1] in self.soft_delete:
            self.soft_delete.remove(self.stack.pop()[1])
        while self.max_heap and self.max_heap[0][1] in self.soft_delete:
            self.soft_delete.remove(heapq.heappop(self.max_heap)[1])
                 

    def pop(self) -> int:
        element = self.stack.pop()
        self.soft_delete.add(element[1])
        self._clean_up()
        return element[0]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        return -self.max_heap[0][0]
        

    def popMax(self) -> int:
        max_element, ele_id = heapq.heappop(self.max_heap)
        self.soft_delete.add(ele_id)
        self._clean_up()
        return -max_element
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()