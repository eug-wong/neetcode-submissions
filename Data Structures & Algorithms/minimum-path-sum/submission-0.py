class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        memo = {(n - 1, m - 1): grid[n - 1][m - 1]}
        def recurse(i, j):
            if i >= n or j >= m:
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]

            res = min(recurse(i + 1, j), recurse(i, j + 1)) + grid[i][j]
            memo[(i, j)] = res
            
            return memo[(i, j)]
        
        return recurse(0, 0)