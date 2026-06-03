import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort start in ascending order
        # use minheap to keep track of interval lengths
        intervals = sorted(intervals)
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)
        heap = []
        heapq.heapify(heap)
        for query in queries:
            for interval in intervals:
                length = interval[1] - interval[0] + 1
                if interval[0] <= query[1]:
                    heapq.heappush(heap, (length, interval[1]))
                else:
                    break

            while True:
                if not heap:
                    res[query[0]] = (-1)
                    break

                candidate = heapq.heappop(heap)
                if candidate[1] >= query[1]:
                    res[query[0]] = candidate[0]
                    break
        
        return res
