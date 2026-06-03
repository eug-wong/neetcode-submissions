class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1, -2, 3, 2, 2]
        # O(m) m = len(nums)
        # 
        # [1, 2, 3, 4, 4], n = 4, 1 <= nums[i] <= 4
        
        for num in nums:
            check = abs(num) - 1
            if nums[check] < 0:
                return abs(num)
            nums[check] = nums[check] * -1
        
        return -1
