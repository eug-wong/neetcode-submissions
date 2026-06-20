class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float('-inf')
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                max_sub = max(max_sub, cur)
        
        return max_sub
