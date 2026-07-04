class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        def recurse(n):
            nonlocal memo
            if n in memo:
                return memo[n]
            
            memo[n] = recurse(n - 1) + recurse(n - 2) + recurse(n - 3)
            
            return memo[n]
        
        return recurse(n)