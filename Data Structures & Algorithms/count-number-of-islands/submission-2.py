class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            nonlocal visited
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            
            if grid[row][col] == "0":
                return

            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_row, new_col = row + d[0], col + d[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    dfs(new_row, new_col)

            return
        
        visited = set()
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    res += 1
        
        return res