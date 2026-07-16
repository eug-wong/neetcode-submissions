class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 1 2 2 3 4 5 3
        # case 1, mid is at peak, return nums[i - 1] <= nums[i] and nums[i] >= nums[i + 1]
        # case 2, not at peak -> 1 2 2 4 5
        # case 3, not at peak -> 3 2 1
        # 1 2 3 2 1
        # 1 1 2 1 2 3 2 1
        # -inf [0] -inf
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 1, len(nums) - 2
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[res]:
                res = mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                res = mid
                l += 1
        
        return res - 1
        