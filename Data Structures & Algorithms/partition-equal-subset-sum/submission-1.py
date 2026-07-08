class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        goal = sum(nums) // 2
        def backtrack(i, cur):
            if i == len(nums):
                return False
            
            if cur == goal:
                return True
            
            # accept
            res = False
            if cur + nums[i] <= goal:
                res = res or backtrack(i + 1, cur + nums[i])
            
            # move on
            res = res or backtrack(i + 1, cur)

            return res
        
        return backtrack(0, 0)