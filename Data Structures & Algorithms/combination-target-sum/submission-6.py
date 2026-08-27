class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(i, cur):
            nonlocal res
            if sum(cur) == target:
                res.append(cur)
                return

            if i == len(nums) or sum(cur) > target:
                return
            
            backtrack(i, cur + [nums[i]])
            backtrack(i + 1, cur)
    
        backtrack(0, [])
        return res