class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exists = set(nums)
        for n in range(1, 100000):
            if n not in exists:
                return n
        
        return 0