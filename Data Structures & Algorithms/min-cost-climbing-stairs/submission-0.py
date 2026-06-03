class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = [1, 2, 3]
        # we want min cost
        # can start at 0 or 1
        # [1, 2, 3]
        #  ^  ^
        # think of this dp,
        # since we can go 1 or 2 steps, we consider min(i - 1, i - 2), then add current cost
        # [1, 2, 4]
        # base cases
        if len(cost) == 2:
            return min(cost)
        
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        return min(dp[-1], dp[-2])