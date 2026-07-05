class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - 2
        while r >= 0 and nums[r] >= nums[r + 1]:
            r -= 1
        
        pivot = r
        
        if pivot != -1:
            minimum = [float('inf'), len(nums) - 1]
            for i in range(pivot, len(nums)):
                if minimum[0] >= nums[i] and nums[i] > nums[pivot]:
                    minimum = [nums[i], i]
            
            if minimum[0] != float('inf'):
                nums[pivot], nums[minimum[1]] = minimum[0], nums[pivot]
        
        l, r = pivot + 1, len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        