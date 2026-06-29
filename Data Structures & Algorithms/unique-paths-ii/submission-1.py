class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1): 1}
        def recurse(i, j):
            nonlocal memo
            if i < 0 or i >= len(obstacleGrid) or j < 0 or j >= len(obstacleGrid[0]):
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = recurse(i + 1, j) + recurse(i, j + 1)
            
            return memo[(i, j)]
        
        return recurse(0, 0)