class Solution:
    def countBits(self, n: int) -> List[int]:
        # n = 4
        # 0 -> 0 0
        # 1 -> 1 1
        # 2 -> 10 1
        # 3 -> 11 2
        # 4 -> 100 1
        # 5 -> 101 2
        # 6 -> 110 2
        # 7 -> 111 3
        # 8 -> 1000 1
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i - offset] + 1
        
        return dp


