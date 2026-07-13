class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.freq = Counter(nums)

    def showFirstUnique(self) -> int:
        copy = self.q.copy()
        while copy:
            cur = copy.popleft()
            if self.freq[cur] == 1:
                return cur
        
        return -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.freq[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
