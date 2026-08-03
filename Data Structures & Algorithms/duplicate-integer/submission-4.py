class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for v in freq.values():
            if v > 1:
                return True
        return False