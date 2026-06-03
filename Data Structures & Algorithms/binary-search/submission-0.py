class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1, 0, 2, 4, 6, 8] sorted target = 4
        # [1, 2, 3] target = 4 -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1