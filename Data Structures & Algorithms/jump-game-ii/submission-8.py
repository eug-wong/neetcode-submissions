class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def recurse(i):
            nonlocal memo
            if i >= len(nums) - 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            res = float('inf')
            for j in range(i + 1, i + nums[i] + 1):
                res = min(res, recurse(j) + 1)

            memo[i] = res
            
            return res
        
        return recurse(0)
            