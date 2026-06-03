class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
        self.cur_min = float("inf")
    
    def push(self, val) -> None:
        self.stack.append(val)
        self.cur_min = min(self.cur_min, val)
        self.mins.append(self.cur_min)
    
    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        if self.mins:
            self.cur_min = self.mins[-1]
        else:
            self.cur_min = float("inf")
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.mins[-1]
    