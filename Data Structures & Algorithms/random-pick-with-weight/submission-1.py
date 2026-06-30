class Solution:

    def __init__(self, w: List[int]):
        temp = [x / sum(w) for x in w]
        self.weights = []
        cur = 0
        for n in temp:
            cur += n
            self.weights.append(cur)


    def pickIndex(self) -> int:
        ran = random.random()
        for i in range(len(self.weights)):
            if i == 0:
                if 0 <= ran <= self.weights[i]:
                    return i
            elif self.weights[i - 1] <= ran <= self.weights[i]:
                return i

        return 0
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()