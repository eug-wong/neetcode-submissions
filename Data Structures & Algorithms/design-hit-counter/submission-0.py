class HitCounter:

    def __init__(self):
        self.pinged = deque()

    def hit(self, timestamp: int) -> None:
        self.pinged.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.pinged and timestamp - self.pinged[0] >= 300:
            self.pinged.popleft()
        
        return len(self.pinged)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
