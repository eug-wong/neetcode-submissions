class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def recurse(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = max(recurse(i + 1), nums[i] + recurse(i + 2))

            return dp[i]
        
        return recurse(0)