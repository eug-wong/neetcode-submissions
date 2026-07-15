class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [-1, -1]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    res[0] = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] <= target:
                if nums[mid] == target:
                    res[1] = mid
                l = mid + 1

        return res
                