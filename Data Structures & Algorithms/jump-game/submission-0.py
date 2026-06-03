class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {0: True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            j = i - 1
            res = False
            while j > -1:
                if i - j <= nums[j]:
                    res = res or dfs(j)
                j -= 1
            
            memo[i] = res
            return memo[i]
        
        return dfs(len(nums) - 1)