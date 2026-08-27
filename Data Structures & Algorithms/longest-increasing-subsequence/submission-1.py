class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # choices
        # if greater than previous, go next
        # if less than previous, accept or go next

        # so really 2 choices
        # if less than previous accept
        # go next
        # check both

        # memoize on index?
        cache = {}
        def recurse(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in cache:
                return cache[(i, prev)]

            res = 0
            if prev == -1 or (prev != -1 and nums[i] > nums[prev]):
                res = max(res, recurse(i + 1, i) + 1)
            
            res = max(res, recurse(i + 1, prev))
            cache[(i, prev)] = res
            return res
        
        return recurse(0, -1)