class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # res = [2, 3, 2, 3]
        #           l. r
        # [0, 1, 2, 2, 3, 0, 4, 2]
        #        l
        #           r
        l, r = 0, 1
        while r < len(nums):
            if nums[r] == val and nums[l] != val:
                l = r
            if nums[r] != val and nums[l] == val:
                nums[l] = nums[r]
                nums[r] = val
                while l < r and nums[l] != val:
                    l += 1
            
            r += 1
        
        return len(nums) - Counter(nums)[val]