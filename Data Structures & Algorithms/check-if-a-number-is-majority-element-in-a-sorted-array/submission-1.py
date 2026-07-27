class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        left, right = -1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                right = mid
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                left = mid
                r = mid - 1
        
        print(right, left, right - left + 1)
        return right - left + 1 > len(nums) // 2 if (right > -1 and left > -1) else False