class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, cur):
            if i == len(nums):
                return 1 if cur == target else 0
            
            if (i, cur) in memo:
                return memo[(i, cur)]
            
            # choose to subtract
            memo[(i, cur)] = dp(i + 1, cur + nums[i]) + dp(i + 1, cur - nums[i])

            return memo[(i, cur)]
        
        return dp(0, 0)