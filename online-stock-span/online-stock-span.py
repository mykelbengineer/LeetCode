class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []
        

    def next(self, price: int) -> int:
        
        curr_price, price_span = price, 1
        
        while self.monotonic_stack and self.monotonic_stack[-1][0] <= curr_price:
            
            prev_price, prev_span = self.monotonic_stack.pop()
            
            price_span += prev_span
            
        self.monotonic_stack.append((curr_price, price_span))
        
        return price_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)