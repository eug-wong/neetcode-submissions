class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def recurse(i):
            nonlocal cache
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(recurse(i + 1), recurse(i + 2) + nums[i])
            return cache[i]
        
        copy = nums
        cache = {}
        nums = copy[1: ]
        res1 = recurse(0)

        cache = {}
        nums = copy[: -1]
        res2 = recurse(0)
        return max(res1, res2)
