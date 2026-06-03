class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find index of pivot, then binary search again?
        # find index of pivot
        l, r = 0, len(nums) - 1
        piv = [nums[0], 0]
        while l <= r:
            if nums[l] <= nums[r]:
                piv = [min(piv[0], nums[l]), l if piv[0] > nums[l] else piv[1]]
                break
            
            m = (l + r) // 2
            piv = [min(piv[0], nums[m]), m if piv[0] > nums[m] else piv[1]]
            # search right mid
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        # piv[1] is pivot point
        nums = nums[piv[1]: ] + nums[: piv[1]]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return (piv[1] + m) % len(nums)
        
        return -1

        '''
        target = 3
        nums = [3, 5, 6, 0, 1, 2]
        pivot = 3

        [0, 1, 2, 3, 5, 6]
        binary search -> 3
        return -> 0
        pivot + binary search % len(nums)
        '''
        