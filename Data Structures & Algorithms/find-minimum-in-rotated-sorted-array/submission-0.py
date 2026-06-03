class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        array = [3, 4, 5, 1, 2]
        l, r, mid 
        cases: 
        l belongs to left, mid belongs to left, r belongs to right
        move r to mid - 1

        l belongs to left, mid belongs to right, r belongs to right
        move l to mid + 1
        '''

        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            # l and mid on left sorted
            if nums[mid] >= nums[l]:
                l = mid + 1
            # r and mid on right sorted
            else:
                r = mid - 1

        return res


