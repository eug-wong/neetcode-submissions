class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        while i < j and j < len(prices):
            max_profit = max(max_profit, prices[j] - prices[i])
            if prices[j] - prices[i] <= 0:
                i = j
            j += 1
        return max_profit