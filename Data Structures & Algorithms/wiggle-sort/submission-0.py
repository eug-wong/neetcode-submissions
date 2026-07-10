class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # on even index, check if nums[i] <= nums[i + 1], cont if true, swap if false
        # on odd index, chek if nums[i] >= nums[i + 1], cont if true, swap if false
        for i in range(len(nums) - 1):
            if i % 2 == 0 and nums[i] > nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
            elif i % 2 == 1 and nums[i] < nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]