class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [1, 2, -3, 4]
        # [1, 2, -6, 4]
        # [1, 2, 3, -1, 4, 1, 10, -2, 1]
        # [1, 2, 6, -1, 4, 4, 40, -2, 1]
        # [1, 2, 3, -6, -24, -96, -40*96, ]
        # previous best, and multiply by current?
        # best we can do at this index -> 
        # what if we kept track of ab est negative and best positive?

        # what are our options
        # mult prev best neg 1
        # mult prev best pos 1
        # begin new sub

        # [1, 2, 3, -1, 4, 1, 10, -2, 1]
        #p[1, 2, 6]
        #n[1, 1, 3]....
        # take the max of p?
        p, n = [0] * len(nums), [0] * len(nums)
        p[0] = nums[0]
        n[0] = nums[0]
        for i in range(1, len(nums)):
            p[i] = max(p[i - 1] * nums[i], n[i - 1] * nums[i], nums[i])
            n[i] = min(p[i - 1] * nums[i], n[i - 1] * nums[i], nums[i])
        
        return max(p)