class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums = [] -> not possible
        # nums = [1] -> 1
        # nums = [1, 2] -> 2
        # nums = [1, 2, 3] -> 4
        # rob houses to maximize money stolen without robbing any adjacent houses

        # nums = [2, 9, 3, 8, 6]
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])
            return memo[i]
        
        return dfs(0)
