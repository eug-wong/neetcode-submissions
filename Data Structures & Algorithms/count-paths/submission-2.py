class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for col in range(n):
            grid[0][col] = 1
        for row in range(m):
            grid[row][0] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

        return grid[m - 1][n - 1]