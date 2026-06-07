class Solution:
    def numSquares(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(20000)
        # lol

        dp = {}
        def recurse(cur):
            if cur == 0:
                return 0
            
            if cur in dp:
                return dp[cur]

            res = cur
            for i in range(1, cur + 1):
                if i * i > cur:
                    break
                res = min(res, 1 + recurse(cur - i * i))
            
            dp[cur] = res
            return res
    
        return recurse(n)