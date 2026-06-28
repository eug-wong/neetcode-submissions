class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        
        pivot = l
        last = len(nums) - 1
        while pivot == 0 and last > 0 and nums[0] == nums[last]:
            last -= 1


        l, r = 0, len(nums) - 1
        if nums[pivot] <= target and nums[last] >= target:
            l = pivot
            r = last
        else:
            r = pivot - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return True

        return False