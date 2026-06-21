class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        def recurse(i, cur):
            # nonlocal memo
            if cur == amount:
                return 1

            if i >= len(coins):
                return 0
            
            if memo[i][cur] != -1:
                return memo[i][cur]
            
            ways = 0
            # accept coin and move on
            if amount - cur >= coins[i]:
                ways += recurse(i + 1, cur)
                ways += recurse(i, cur + coins[i])
            
            memo[i][cur] = ways

            return ways
        
        return recurse(0, 0)

            