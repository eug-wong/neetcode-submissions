class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def recurse(amount):
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]
            
            res = float('inf')
            for c in coins:
                if amount - c >= 0:
                    res = min(res, recurse(amount - c) + 1)
            
            cache[amount] = res
            return res
        
        min_coins = recurse(amount) 
        return min_coins if min_coins != float('inf') else -1