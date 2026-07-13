class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.freq = Counter(nums)

    def showFirstUnique(self) -> int:
        while self.q and self.freq[self.q[0]] > 1:
            c = self.q.popleft()

        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.freq[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
