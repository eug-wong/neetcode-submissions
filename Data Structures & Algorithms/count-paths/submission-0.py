class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 3x + 6y = 21
        # 3x + 3y = 6
        # x = -3, y = 5
        # m = 1 n = 1 1
        # m = 2 n = 2 2
        # m = 3 n = 3 6
        # n!/(m-1)!
        return math.factorial(m + n - 2)//(math.factorial(n - 1) * math.factorial(m - 1))