class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        for row in self.matrix:
            t = []
            cur = 0
            for v in row:
                t.append(cur + v)
                cur += v
            self.prefix.append(t)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 3  3  4  8  10
        # 5  11 14 16 17
        # 1  3  3  4  9
        # 4  5  5  6  13
        # 1  1  4  4  9
        # [[3, 0, 1, 4, 2], 
        #  [5, 6, 3, 2, 1], 
        #. [1, 2, 0, 1, 5], 
        #. [4, 1, 0, 1, 7], 
        #. [1, 0, 3, 0, 5]]
        # (2, 1) - (4, 3)
        res = 0
        for r in range(row1, row2 + 1):
            if col1 - 1 >= 0:
                res += (self.prefix[r][col2] - self.prefix[r][col1 - 1])
            else:
                res += self.prefix[r][col2]
        
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)