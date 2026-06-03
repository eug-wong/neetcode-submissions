class Solution:
    def climbStairs(self, n: int) -> int:
        # 2 choices, 1 or 2 steps at a time
        # distinct ways to clibm to staircase
        # n = 2
        # [1, 2]
        # n = 3
        # [1, 2, 3]
        # n = 4
        # [1, 2, 3, = n - 1+ n-2]
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        
        for i in range (2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]