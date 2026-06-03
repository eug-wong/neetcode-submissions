class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]
        def backtrack(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]
            
            res = backtrack(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + backtrack(i + 1, i))
            
            memo[i][j + 1] = res
            return res
        
        return backtrack(0, -1)