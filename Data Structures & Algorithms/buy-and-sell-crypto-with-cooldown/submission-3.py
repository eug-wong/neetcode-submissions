class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def recurse(i, hold):
            if i >= len(prices):
                return 0
            
            if (i, hold) in memo:
                return memo[(i, hold)]
            
            res = 0
            # choices
            # buy i + 1
            if hold == -1:
                res = max(res, -prices[i] + recurse(i + 1, 1))

            # pass i + 1
            res = max(res, recurse(i + 1, hold))

            # sell i + 2
            if hold != -1:
                res = max(res, prices[i] + recurse(i + 2, -1))
            
            memo[(i, hold)] = res

            return res
        
        return recurse(0, -1)