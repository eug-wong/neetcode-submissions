class Solution:
    def rob(self, nums: List[int]) -> int:
        # backtracking approach is
        # 2 choices:
        # rob current house and skip next
        # skip current house
        cache = {}
        def recurse(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            res = recurse(i + 1)
            res = max(res, recurse(i + 2) + nums[i])
            cache[i] = res
            return res
        
        return recurse(0)