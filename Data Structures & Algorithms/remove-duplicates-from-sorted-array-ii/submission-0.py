class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            start, cur = r, nums[r]
            while r < len(nums) and cur == nums[r]:
                r += 1
            
            for _ in range(min(2, r - start)):
                nums[l] = cur
                l += 1
        
        return l