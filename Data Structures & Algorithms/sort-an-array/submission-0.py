class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # mergesort
        # return sorted(nums)

        # merge sort
        # divide into 2
        # linear sort between two lists and return
        def div(nums):
            if len(nums) == 1:
                return nums
            
            # linear sort
            mid = len(nums) // 2
            l1 = div(nums[0 :mid])
            l2 = div(nums[mid: ])
            
            res = []
            while l1 and l2:
                if l2[0] <= l1[0]:
                    res.append(l2[0])
                    l2 = l2[1: ]
                else:
                    res.append(l1[0])
                    l1 = l1[1: ]
            
            if l1:
                res += l1
            else:
                res += l2
            
            return res

        return div(nums)