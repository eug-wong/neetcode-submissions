class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0: 0, 1: 0}
        l = 0
        res1 = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while l <= r and freq[1] > goal:
                freq[nums[l]] -= 1
                l += 1
            
            res1 += (r - l + 1)

        freq = {0: 0, 1: 0}
        res2 = 0
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while l <= r and freq[1] > goal - 1:
                freq[nums[l]] -= 1
                l += 1
            
            res2 += (r - l + 1)
        
        return res1 - res2