class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        dist = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    continue
                
                if grid[i][j] == -1:
                    continue
                
                if (i, j) in visited:
                    continue
                
                visited.add((i, j))
                grid[i][j] = min(grid[i][j], dist)

                q.append((i - 1, j))
                q.append((i + 1, j))
                q.append((i, j - 1))
                q.append((i, j + 1))
            
            dist += 1
        