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
        i = 0
        for query in queries:
            while i < len(intervals) and intervals[i][0] <= query[1]:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < query[1]:
                heapq.heappop(heap)
            
            res[query[0]] = heap[0][0] if heap else -1
        
        return res
