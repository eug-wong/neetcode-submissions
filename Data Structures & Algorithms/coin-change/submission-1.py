class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # i see backtrack recursive sol. n^2
        # can't be greedy even if it looks right
        # maybe start with backtrack then add memoization?
        # if you're at a current sum, maybe you already know the min number of coins for that sum
        # so then we can keep track of that to prune branches in decision tree?
        # memo should keep track of the 
        memo = {0: 0}
        def dfs(total):
            nonlocal memo
            nonlocal amount
            nonlocal coins
            if total in memo:
                return memo[total]
            if total < 0:
                return float('inf')
            
            res = float('inf')
            
            for c in coins:
                if total - c >= 0:
                    res = min(res, dfs(total - c) + 1)

            memo[total] = res
            return memo[total]
        
        return dfs(amount) if dfs(amount) != float('inf') else -1