class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        lowest = float('inf')
        cur = 0
        while r < len(nums):
            cur += nums[r]
            while cur >= target:
                lowest = min(lowest, r - l + 1)
                cur -= nums[l]
                l += 1
            
            r += 1
        
        return lowest if lowest != float('inf') else 0