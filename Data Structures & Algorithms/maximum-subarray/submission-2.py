class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        cur = 0
        res = float('-inf')
        while r < len(nums):
            cur += nums[r]
            res = max(res, cur)
            # handle what happens if cur becomes negative
            while cur < 0:
                cur -= nums[l]
                l += 1
            r += 1
        
        return res
