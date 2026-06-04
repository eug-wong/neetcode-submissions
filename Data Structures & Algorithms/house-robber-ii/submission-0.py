class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dp(arr):
            memo = {}
            def solve(i):
                if i < 0:
                    return 0
                if i in memo:
                    return memo[i]
                res = max(solve(i - 2) + arr[i], solve(i - 1))
                memo[i] = res
                return res
            return solve(len(arr) - 1)
        
        return max(dp(nums[1:]), dp(nums[:-1]))