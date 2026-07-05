class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}
        def recurse(i, j):
            nonlocal memo
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            down, right, diagonal = recurse(i + 1, j), recurse(i, j + 1), recurse(i + 1, j + 1)
            memo[(i, j)] = 0
            if matrix[i][j] == "1":
                memo[(i, j)] = 1 + min(down, right, diagonal)

            return memo[(i, j)]
        
        recurse(0, 0)
        return max(memo.values()) ** 2