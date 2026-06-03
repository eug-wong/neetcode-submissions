class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        for k, v in freq.items():
            if v > n / 2:
                return k
        
        return -42