class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # memoize # of ways to generate target from current sum
        memo = defaultdict(int)
        def recurse(remainder):
            if remainder < 0:
                return 0
            
            if remainder == 0:
                return 1

            if remainder in memo:
                return memo[remainder]

            res = 0
            for num in nums:
                res += recurse(remainder - num)
            
            memo[remainder] = res
            return res
        
        return recurse(target)