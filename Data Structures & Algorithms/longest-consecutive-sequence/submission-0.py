class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
        
        longest = 0
        while exists:
            minimum = min(exists)
            streak = 0
            while minimum in exists:
                exists.remove(minimum)
                minimum += 1
                streak += 1
            longest = max(streak, longest)
        
        return longest