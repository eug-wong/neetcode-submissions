class Solution:
    def rob(self, nums: List[int]) -> int:
        # house robber... classico hahahahahahahahahah
        # cannot rob two adjacent houses
        # maximum money
        # [1, 1, 3, 3]
        # dp of max money at each house
        # [1, 1, 3, 4]           
        # max of the previous previous two plus current
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i - 1]
        print(dp)
        return max(dp[-1], dp[-2])
