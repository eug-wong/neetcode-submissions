class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def recurse(i, holding):
            # if holding, sell
            # either holding or not holding, continue
            # if not holding, buy or continue
            if i == len(prices):
                return 0
            
            if (i, holding) in dp:
                return dp[(i, holding)]

            res = 0
            if holding:
                res = max(res, recurse(i + 1, False) + prices[i])
            else:
                res = max(res, recurse(i + 1, True) - prices[i])
            
            res = max(res, recurse(i + 1, holding))
            dp[(i, holding)] = res
            
            return res
        
        return recurse(0, False)
