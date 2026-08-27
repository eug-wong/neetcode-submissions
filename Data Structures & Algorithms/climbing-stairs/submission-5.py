class Solution:
    def climbStairs(self, n: int) -> int:
        
        # recursion relation is R(n) = R(n - 1) + R(n - 2)
        # base cases are n = 0, n = 1, n = 2
        memo = {0: 0, 1: 1, 2: 2}
        def recurse(n):
            nonlocal memo
            if n in memo:
                return memo[n]
            
            memo[n] = recurse(n - 1) + recurse(n - 2)
            return memo[n]
        
        return recurse(n)