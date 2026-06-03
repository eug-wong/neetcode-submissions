class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def isValid(i, j):
            return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])

        def dfs(i, j):
            nonlocal memo
            if (i, j) in memo:
                return memo[(i, j)]

            res = 1
            if isValid(i + 1, j) and matrix[i + 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(i + 1, j))
            
            if isValid(i, j + 1) and matrix[i][j + 1] > matrix[i][j]:
                res = max(res, 1 + dfs(i, j + 1))
            
            if isValid(i - 1, j) and matrix[i - 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(i - 1, j))
            
            if isValid(i, j - 1) and matrix[i][j - 1] > matrix[i][j]:
                res = max(res, 1 + dfs(i, j - 1))
            
            memo[(i, j)] = res
            return res
        
        memo = {}
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))
        
        return ans