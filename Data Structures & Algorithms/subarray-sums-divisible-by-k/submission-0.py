class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # [4, 9, 9, 7, 4, 5]
        # [0, 4, 9, 9, 7, 4, 5]

        prefix = 0
        remains = defaultdict(int)
        remains[0] = 1
        res = 0
        for num in nums:
            prefix += num
            remainder = prefix % k
            res += remains[remainder]
            remains[remainder] += 1
        
        return res