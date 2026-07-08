class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r, longest = 0, 0
        while r < len(nums):
            cur = 0
            while r < len(nums) and nums[r] == 1:
                r += 1
                cur += 1
            
            longest = max(longest, cur)
            r += 1
        
        return longest