class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        cur = 0
        maximum = 0
        while r < len(nums):
            cur += nums[r]
            while nums[r] * (r - l + 1) > cur + k:
                cur -= nums[l]
                l += 1
                
            maximum = max(maximum, r - l + 1)
            r += 1
        
        return maximum