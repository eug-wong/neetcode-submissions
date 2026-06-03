class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def recurse(i, bought):
            if i == len(prices):
                return 0
            
            if (i, bought) in dp.keys():
                return dp[(i, bought)]
            
            # do nothing, skip
            res = recurse(i + 1, bought)
            # if holding stock, sell at current price and add to profit
            if bought:
                res = max(res, prices[i] + recurse(i + 1, False))
            else:
                res = max(res, -prices[i] + recurse(i + 1, True))
            
            dp[(i, bought)] = res
            return res
        
        return recurse(0, False)