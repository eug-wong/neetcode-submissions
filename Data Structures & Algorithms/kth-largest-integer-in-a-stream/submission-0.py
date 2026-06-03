class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = [-1 * x for x in nums]
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, -1 * val)
        t = []
        res = None
        for _ in range(self.k):
            res = heapq.heappop(self.h)
            t.append(res)
        
        for v in t:
            heapq.heappush(self.h, v)
        
        return -1 * res
