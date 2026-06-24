class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for m in range(len(nums)):
            for n in range(m, len(nums)):
                cur = nums[m] + nums[n]
                l, r = 0, len(nums) - 1
                while l < r:
                    if len({m, n, r, l}) == 4 and cur + nums[l] + nums[r] == target:
                        if sorted([nums[m], nums[n], nums[l], nums[r]]) not in res:
                            res.append([nums[m], nums[n], nums[l], nums[r]])
                        l += 1
                    elif cur + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        
        return res