class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transposed = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                transposed[i][j] = matrix[j][i]

        return transposed