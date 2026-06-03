import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort start in ascending order
        # use minheap to keep track of interval lengths
        intervals = sorted(intervals)
        res = []
        for query in queries:
            heap = []
            heapq.heapify(heap)
            for interval in intervals:
                length = interval[1] - interval[0] + 1
                if interval[0] <= query:
                    heapq.heappush(heap, (length, interval[1]))
                else:
                    break
            while True:
                if not heap:
                    res.append(-1)
                    break

                candidate = heapq.heappop(heap)
                if candidate[1] >= query:
                    res.append(candidate[0])
                    break
        
        return res
