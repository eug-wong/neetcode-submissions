class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        zeroes = 0
        longest = 0
        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest