class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            length = 0
            while num in nums:
                num = num + 1
                length += 1
            longest = max(longest, length)
        
        return longest