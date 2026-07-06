class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            goal = -1 * nums[i]
            while l < r:
                if nums[l] + nums[r] == goal:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > goal:
                    r -= 1
                else:
                    l += 1
        
        return list(res)