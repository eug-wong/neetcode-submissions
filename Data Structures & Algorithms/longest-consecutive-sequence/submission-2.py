class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for n in nums:
            l = 1
            while n + 1 in seen:
                l += 1
                n += 1
            longest = max(longest, l)
    
        return longest
        