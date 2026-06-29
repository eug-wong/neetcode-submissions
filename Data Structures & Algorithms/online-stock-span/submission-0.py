class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        temp = []
        cur = 1
        while self.stack and self.stack[-1] <= price:
            temp.append(self.stack.pop())
            cur += 1
        
        self.stack = self.stack + temp[::-1]
        self.stack.append(price)
        return cur



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)