class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur, longest = 0, 0
        for num in nums:
            cur = cur + 1 if num == 1 else 0
            longest = max(longest, cur)
        
        return longest