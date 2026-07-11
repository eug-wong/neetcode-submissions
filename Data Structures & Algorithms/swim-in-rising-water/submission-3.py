class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        l, r = max(grid[n - 1][n - 1], grid[0][0]), max([max(row) for row in grid])
        res = r
        while l <= r:
            mid = (l + r) // 2
            q = deque([(0, 0)])
            visited = set()
            reached = False
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur == (n - 1, n - 1):
                        reached = True
                    visited.add(cur)
                    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = cur[0] + d[0], cur[1] + d[1]
                        if (0 <= x < n 
                            and 0 <= y < n 
                            and grid[x][y] <= mid 
                            and (x, y) not in visited and (x, y) not in q):
                            q.append((x, y))      
            if reached:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
