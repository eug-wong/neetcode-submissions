class Solution:
    import math
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        heapq.heapify(dists)
        for point in points:
            dist = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
            heapq.heappush(dists, [dist, point])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(dists)[1])
        
        return res