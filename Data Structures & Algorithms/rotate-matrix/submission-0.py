class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1  2  3  4  5
        # 6  7  8  9  10
        # 11 12 13 14 15
        # 16 17 18 19 20
        # 21 22 23 24 25
        #
        # [0][0] -> [0][n] -> [n][n] -> [n][0]
        # [0][1] -> [1][n] -> [n][n - 1] -> [n - 1][0]
        # [i][j] -> [j][n] -> [n][n - j] -> [n - j][0]

        # [0][0] -> [0][n] -> [n][n] -> [n][0]
        # [1][1] -> [1][n - 1] -> [n - 1][n - 1] -> [n - 1][1]
        # [0][1] -> [1][n] -> [n][n - 1] -> [n - 1][0]
        # [i][j] -> [n][n - i] -> [n - i][n - j] -> [n - i][j]
        # [2][3] -> [3][2] -> [2][1] -> [1][2]
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                save = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = save
            
            r -= 1
            l += 1
