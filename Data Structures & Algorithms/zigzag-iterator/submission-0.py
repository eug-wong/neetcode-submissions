class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q1 = deque(v1)
        self.q2 = deque(v2)
        self.it = True # true == v1, false == v2

    def next(self) -> int:
        if self.q1 and not self.q2:
            return self.q1.popleft()
        
        if self.q2 and not self.q1:
            return self.q2.popleft()

        if self.it and self.q1:
            self.it = False
            return self.q1.popleft()
        elif self.q2:
            self.it = True
            return self.q2.popleft()

    def hasNext(self) -> bool:
        return self.q1 or self.q2
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
