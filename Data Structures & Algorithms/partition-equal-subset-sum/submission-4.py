class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        cache = {}
        def recurse(i, cur):
            if cur == target:
                return True
            
            if cur > target:
                return False
            
            if i >= len(nums):
                return False
            
            if (i, cur) in cache:
                return cache[(i, cur)]
            
            # accept
            res = recurse(i + 1, cur + nums[i])
            # go next
            res = res or recurse(i + 1, cur)
            cache[(i, cur)] = res
            return res
        
        return recurse(0, 0)