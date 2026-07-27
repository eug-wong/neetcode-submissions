class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        freq = Counter(nums)
        return freq[target] > len(nums) // 2