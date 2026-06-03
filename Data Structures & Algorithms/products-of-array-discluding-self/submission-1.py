class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix + suffix
        prefix = []
        cur = 1
        for n in nums:
            prefix.append(cur)
            cur = cur * n
        
        suffix = [0] * len(nums)
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = cur
            cur = cur * nums[i]
        
        res = []
        for p, s in zip(prefix, suffix):
            res.append(p * s)

        return res