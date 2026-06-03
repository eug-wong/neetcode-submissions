class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        factor = 1
        for i in range(len(nums)):
            pre[i] = factor
            factor *= nums[i]
        
        factor = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = factor
            factor *= nums[i]
            print(suf)
        
        out = []
        for i in range(len(nums)):
            out.append(pre[i] * suf[i])
        
        return out
        