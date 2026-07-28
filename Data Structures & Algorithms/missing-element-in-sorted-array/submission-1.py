class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lowest = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = r - (r - l) // 2
            if nums[mid] - lowest - mid < k:
                l = mid
            else:
                r = mid - 1
        
        return lowest + k + l
