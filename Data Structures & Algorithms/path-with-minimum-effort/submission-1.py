class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        heap = [[0, (0, 0)]]
        heapq.heapify(heap)

        while heap:
            cur = heapq.heappop(heap)
            if cur[1] in visited:
                continue
            
            visited.add(cur[1])
            
            if cur[1] == (len(heights) - 1, len(heights[0]) - 1):
                return cur[0]
            
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = cur[1][0] + d[0], cur[1][1] + d[1]
                if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0]) and (i, j) not in visited:
                    heapq.heappush(heap, [max(cur[0], abs(heights[cur[1][0]][cur[1][1]] - heights[i][j])), (i, j)])
        
        return -1