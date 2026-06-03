class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        maximum = float('-inf')
        cur = 0
        while r < len(nums):
            cur += nums[r]
            maximum = max(maximum, cur)
            if cur < 0:
                cur = 0
            
            r += 1
        return maximum