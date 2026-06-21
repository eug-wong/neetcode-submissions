class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        total = 0
        heap = [(0, 0)]
        heapq.heapify(heap)
        while len(visited) < len(points):
            cur = heapq.heappop(heap)
            while cur[1] in visited:
                cur = heapq.heappop(heap)
            x, y = points[cur[1]]
            total += cur[0]
            visited.add(cur[1])
            for i, (x1, y1) in enumerate(points):
                if (x1, y1) not in visited:
                    heapq.heappush(heap, (abs(x1 - x) + abs(y1 - y), i))
        
        return total
