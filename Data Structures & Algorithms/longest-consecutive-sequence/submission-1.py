class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
        
        longest = 0
        for num in exists:
            if num - 1 not in exists:
                streak = 0
                while num in exists:
                    streak += 1
                    num += 1
                longest = max(longest, streak)
        
        return longest