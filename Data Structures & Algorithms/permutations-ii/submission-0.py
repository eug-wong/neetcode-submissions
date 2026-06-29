class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        explored = set()
        def recurse(cur, nums):
            nonlocal res
            nonlocal n
            if len(cur) == n:
                res.append(cur)
            
            if tuple(cur) in explored:
                return
            
            explored.add(tuple(cur))
            
            for i, num in enumerate(nums):
                recurse(cur + [num], nums[: i] + nums[i + 1: ])
            
            return
        
        recurse([], nums)
        
        return res