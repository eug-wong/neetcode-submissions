class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur, length, options):
            nonlocal res
            if length == len(nums):
                res.append(cur)
                return
            
            for i, option in enumerate(options):
                backtrack(cur + [option], length + 1, options[: i] + options[i + 1: ])
            
            return
        
        res = []
        backtrack([], 0, nums)

        return res