class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        n1, n2 = nums[0], nums[1]
        inc = False
        if n2 >= n1:
            inc = True
        for i in range(1, len(nums)):
            if inc and nums[i] < nums[i - 1]:
                return False
            elif not inc and nums[i] > nums[i - 1]:
                return False
        
        return True