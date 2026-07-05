class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(coord):
            nonlocal res
            nonlocal visited
            i, j = coord
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            
            if grid[i][j] == 0:
                return

            if coord in visited:
                return
            
            visited.add(coord)
            
            res += 1
            
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs((i + d[0], j + d[1]))


        rows, cols = len(grid), len(grid[0])
        to_visit = set()
        for r in range(rows):
            if grid[r][0] == 1:
                to_visit.add((r, 0))
            if grid[r][cols - 1] == 1:
                to_visit.add((r, cols - 1))
        for c in range(cols):
            if grid[0][c] == 1:
                to_visit.add((0, c))
            if grid[rows - 1][c] == 1:
                to_visit.add((rows - 1, c))
        
        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total += 1
        
        visited = set()
        res = 0
        for coord in to_visit:
            if coord not in visited:
                dfs(coord)

        return total - res