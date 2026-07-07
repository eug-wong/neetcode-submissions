class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        if 1 in freq.values():
            return -1
            
        res = 0
        for k, v in freq.items():
            minimum = float('inf')
            subs = 0
            # print(k)
            while v > 0:
                if v % 2 == 0:
                    minimum = min(minimum, v // 2 + subs)
                if v % 3 == 0:
                    minimum = min(minimum, v // 3 + subs)
                v -= 3
                subs += 1
                # print("v", v)
            res += minimum
            # print("min", minimum)

        return res