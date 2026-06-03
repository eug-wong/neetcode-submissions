class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        # [2 -1 1 2]
        #  
        count = defaultdict(int)
        count[0] = 1
        cur = 0
        ans = 0
        for x in nums:
            cur += x
            ans += count[cur - k]
            count[cur] += 1
        return ans