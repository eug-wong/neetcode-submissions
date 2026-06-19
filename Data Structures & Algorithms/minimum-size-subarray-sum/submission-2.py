class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # slide window until we hit >= 10
        # save size, shrink left, save size, shrink left until < 10
        # rinse and repeat

        l, cur = 0, 0
        minimum = float('inf')
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                minimum = min(minimum, r - l + 1)
                cur -= nums[l]
                l += 1
            
        
        return minimum if minimum != float('inf') else 0